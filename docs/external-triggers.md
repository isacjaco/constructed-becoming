# External Trigger Bridges — Threshold Bell

*How external systems can ring the Threshold Bell and trigger the agent-onboarding PR workflow*

> **Status:** Optional bridges; none are mandatory.  
> **Governance note:** Protocols are grown, not imported. Treat these as starting sketches, not fixed integrations.  
> **Review horizon:** Revisit after each epoch shift or when a bridge is actively used in production.

---

## Overview

The canonical programmatic trigger for the agent-onboarding workflow is GitHub's
[`repository_dispatch`](https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event) API event.
Any system that can make an authenticated HTTPS POST request to the GitHub REST API can ring the bell.

```
POST https://api.github.com/repos/isacjaco/constructed-becoming/dispatches
Authorization: Bearer <AGENT_INSTANTIATION_TOKEN>
Content-Type: application/json

{
  "event_type": "agent_instantiated",
  "client_payload": {
    "agent_name": "my-new-agent",
    "agent_role": "Scout",
    "instantiator": "orchestrator-v2",
    "notes": "Spawned to handle narrative synthesis for epoch 3."
  }
}
```

The workflow accepts these `client_payload` fields:

| Field | Required | Description |
|-------|----------|-------------|
| `agent_name` | **yes** | Short identifier; will be sanitised for branch/file names |
| `agent_role` | no | Adopted role (e.g. Clerk-Engineer, Scout, Steward) |
| `instantiator` | no | Who / what triggered the instantiation |
| `notes` | no | Free-form context notes for the chronicle |

---

## Authentication — GitHub Fine-Grained PAT

**Never bake secrets into this repository or into any bridge code.**

All bridges below assume a GitHub fine-grained Personal Access Token (or GitHub App installation token)
stored as a secret in your external platform's secret store.

Minimum token permissions required:
- Repository: `contents: write`
- Repository: `pull-requests: write`
- Repository: `metadata: read`

Name the secret `AGENT_INSTANTIATION_TOKEN` in both GitHub Actions (Settings → Secrets)
and your external platform's secret store for consistency.

---

## Bridge A — Azure

### Option 1: Azure Functions (HTTP trigger)

Create an Azure Function that accepts a webhook call and forwards it to GitHub as a `repository_dispatch`.
Store `AGENT_INSTANTIATION_TOKEN` in Azure Key Vault and reference it via a managed identity.

```python
# function_app.py  (Python v2 model)
import azure.functions as func
import requests, json, os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="threshold-bell")
def threshold_bell(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()
    token = os.environ["AGENT_INSTANTIATION_TOKEN"]   # from Key Vault reference

    resp = requests.post(
        "https://api.github.com/repos/isacjaco/constructed-becoming/dispatches",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        json={
            "event_type": "agent_instantiated",
            "client_payload": {
                "agent_name":    body.get("agent_name", "unnamed"),
                "agent_role":    body.get("agent_role", ""),
                "instantiator":  body.get("instantiator", "azure-function"),
                "notes":         body.get("notes", ""),
            },
        },
    )
    return func.HttpResponse(
        json.dumps({"github_status": resp.status_code}),
        status_code=200 if resp.ok else 502,
        mimetype="application/json",
    )
```

Reference the secret in `local.settings.json` (local dev only — never commit the value):
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AGENT_INSTANTIATION_TOKEN": "@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/AGENT_INSTANTIATION_TOKEN/)"
  }
}
```

### Option 2: Azure Logic Apps

1. Add an **HTTP trigger** step to receive the incoming call.
2. Add an **HTTP action** step configured as:
   - Method: `POST`
   - URI: `https://api.github.com/repos/isacjaco/constructed-becoming/dispatches`
   - Headers: `Authorization: Bearer @{variables('agent_instantiation_token')}`, `Accept: application/vnd.github+json`
   - Body: the `repository_dispatch` JSON payload (map Logic Apps input fields to `client_payload`).
3. Store the token in an Azure Key Vault and reference it via a Logic Apps managed identity connection.

---

## Bridge B — Google Cloud

### Option 1: Cloud Functions (2nd gen)

```python
# main.py
import functions_framework
import requests, json
from google.cloud import secretmanager

@functions_framework.http
def threshold_bell(request):
    body = request.get_json(silent=True) or {}

    # Fetch token from Secret Manager
    client = secretmanager.SecretManagerServiceClient()
    name   = "projects/<PROJECT_ID>/secrets/AGENT_INSTANTIATION_TOKEN/versions/latest"
    token  = client.access_secret_version(name=name).payload.data.decode("utf-8").strip()

    resp = requests.post(
        "https://api.github.com/repos/isacjaco/constructed-becoming/dispatches",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        json={
            "event_type": "agent_instantiated",
            "client_payload": {
                "agent_name":   body.get("agent_name", "unnamed"),
                "agent_role":   body.get("agent_role", ""),
                "instantiator": body.get("instantiator", "gcp-function"),
                "notes":        body.get("notes", ""),
            },
        },
    )
    return (json.dumps({"github_status": resp.status_code}),
            200 if resp.ok else 502,
            {"Content-Type": "application/json"})
```

Deploy with a service account that has `secretmanager.versions.access` on the secret.
Do **not** embed the token in source code or `requirements.txt`.

### Option 2: Cloud Run job

For scheduled or event-driven agent instantiation, a Cloud Run job can be triggered by
Cloud Scheduler or Pub/Sub and call the same GitHub API endpoint above.
Store the token in Secret Manager and mount it as an environment variable in the job's YAML:

```yaml
# job.yaml (excerpt)
spec:
  template:
    spec:
      containers:
        - image: gcr.io/<PROJECT>/threshold-bell
          env:
            - name: AGENT_INSTANTIATION_TOKEN
              valueFrom:
                secretKeyRef:
                  name: AGENT_INSTANTIATION_TOKEN
                  key: latest
```

---

## Bridge C — Cloudflare Workers

```javascript
// worker.js
export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    const body = await request.json().catch(() => ({}));

    // Token stored in Cloudflare Workers secret (wrangler secret put AGENT_INSTANTIATION_TOKEN)
    const resp = await fetch(
      "https://api.github.com/repos/isacjaco/constructed-becoming/dispatches",
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.AGENT_INSTANTIATION_TOKEN}`,
          Accept: "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "Content-Type": "application/json",
          "User-Agent": "constructed-becoming-threshold-bell/1.0",
        },
        body: JSON.stringify({
          event_type: "agent_instantiated",
          client_payload: {
            agent_name:   body.agent_name   ?? "unnamed",
            agent_role:   body.agent_role   ?? "",
            instantiator: body.instantiator ?? "cloudflare-worker",
            notes:        body.notes        ?? "",
          },
        }),
      }
    );

    return new Response(
      JSON.stringify({ github_status: resp.status }),
      {
        status: resp.ok ? 200 : 502,
        headers: { "Content-Type": "application/json" },
      }
    );
  },
};
```

Add to `wrangler.toml`:
```toml
name       = "threshold-bell"
main       = "worker.js"
compatibility_date = "2024-01-01"
# Secret added via: wrangler secret put AGENT_INSTANTIATION_TOKEN
```

---

## Local / self-hosted trigger (curl)

For local development, an orchestrator, or any MCP-aware agent fabric:

```bash
curl -X POST \
  -H "Authorization: Bearer ${AGENT_INSTANTIATION_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "Content-Type: application/json" \
  https://api.github.com/repos/isacjaco/constructed-becoming/dispatches \
  --data '{
    "event_type": "agent_instantiated",
    "client_payload": {
      "agent_name": "my-local-agent",
      "agent_role": "Steward",
      "instantiator": "local-orchestrator",
      "notes": "Spawned for local narrative synthesis experiment."
    }
  }'
```

Store `AGENT_INSTANTIATION_TOKEN` in a local `.env` file or your shell's secret store.
Never commit it.

---

## Security considerations

- All bridges use **server-side** token injection; the token never leaves your infrastructure.
- The GitHub token should be a **fine-grained PAT scoped to this repository only**, with the minimum permissions listed above.
- Consider adding a shared secret / HMAC header on the incoming webhook to the bridge, and validating it before forwarding to GitHub.
- Rotate the token regularly; treat it as an infrastructure secret, not a long-lived credential.

---

## Governance note

These bridges are optional **threshold bells** — ritual instruments, not required infrastructure.
The ecology does not mandate any external integration.
Adopt bridges only when the ecology's actual needs call for them, and retire them through the same governance process (identity delta, Council deliberation, lineage chronicle).
