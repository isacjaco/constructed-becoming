# External Triggers — Ringing the Threshold Bell

*How external systems can trigger agent onboarding in Constructed‑Becoming*

> Protocols are grown, not handed down. This document describes the current emergent convention
> for triggering the onboarding workflow from outside GitHub. Review horizon: one epoch or
> thirty days, whichever comes first.

---

## Overview

The onboarding workflow (`.github/workflows/agent-onboarding.yml`) can be triggered in two ways:

1. **Manual** — via `workflow_dispatch` in the GitHub Actions UI.
2. **Programmatic** — via `repository_dispatch` (event type: `agent_instantiated`).

External systems — Azure Functions/Logic Apps, GCP Cloud Run/Cloud Functions, Cloudflare Workers —
act as **bridges**: they authenticate with GitHub and POST to the dispatch endpoint.
The bridge is a conduit, not a sovereign.

---

## Recommended auth: GitHub App (preferred)

Using a **GitHub App** is the recommended approach. GitHub Apps grant fine-grained, scoped
permissions, support installation-level access tokens (short-lived, no long-lived secrets),
and are auditable.

### Why not a Personal Access Token (PAT)?

PATs are long-lived, tied to a specific user account, and grant broad permissions if scoped
incorrectly. They are acceptable as a **fallback** in low-risk environments, but should not
be the default. See the [PAT fallback](#pat-fallback-optional) section below.

---

## GitHub App setup (high-level)

### 1. Create the GitHub App

1. Go to **GitHub → Settings → Developer settings → GitHub Apps → New GitHub App**.
2. Set a name (e.g., `constructed-becoming-bridge`).
3. Set the Homepage URL to your repo URL.
4. Under **Permissions → Repository permissions**, grant:
   - **Contents**: Read and write (needed to push the chronicle branch).
   - **Pull requests**: Read and write (needed to open the PR).
   - **Metadata**: Read-only (required by default).
5. Under **Where can this GitHub App be installed?**, choose **Only on this account**.
6. Save and note the **App ID**.
7. Generate a **private key** (PEM file) — store it in your secret manager, not in the repo.

### 2. Install the GitHub App

1. Go to the App's settings page → **Install App**.
2. Install it on the target repository (`constructed-becoming`).
3. Note the **Installation ID** (visible in the URL after installation:
   `https://github.com/settings/installations/<installation_id>`).

### 3. Generate an installation access token (JWT → token flow)

GitHub Apps authenticate in two steps:

**Step A — Create a signed JWT (valid for up to 10 minutes)**

```
header  = { "alg": "RS256", "typ": "JWT" }
payload = {
  "iat": <now - 60 seconds>,   # issued at (allow clock skew)
  "exp": <now + 600 seconds>,  # expires in 10 minutes
  "iss": "<APP_ID>"
}
jwt = RS256_sign(header + "." + payload, private_key_pem)
```

**Step B — Exchange JWT for an installation access token (valid for 1 hour)**

```
POST https://api.github.com/app/installations/<INSTALLATION_ID>/access_tokens
Authorization: Bearer <JWT>
Accept: application/vnd.github+json
```

Response:

```json
{
  "token": "ghs_...",
  "expires_at": "2026-04-10T17:00:00Z"
}
```

Use `token` as the `Authorization: Bearer` value for the dispatch call below.

### 4. Call the dispatch endpoint

```
POST https://api.github.com/repos/{owner}/{repo}/dispatches
Authorization: Bearer <installation_access_token>
Accept: application/vnd.github+json
Content-Type: application/json

{
  "event_type": "agent_instantiated",
  "client_payload": {
    "agent_name": "my-new-agent",
    "agent_role": "Scout",
    "instantiator": "azure-bridge",
    "notes": "Triggered by Azure Logic App on new deployment event."
  }
}
```

**Payload fields:**

| Field | Required | Description |
|---|---|---|
| `agent_name` | ✅ | Agent identifier. Will be sanitised to kebab-case for branch/filename. |
| `agent_role` | ❌ | Adopted role (e.g., Clerk, Scout, Steward). |
| `instantiator` | ❌ | Who or what is ringing the bell. |
| `notes` | ❌ | Free-form notes for the instantiation header. |

---

## Platform bridge examples

The examples below are minimal reference snippets. They show the pattern, not a
production-hardened implementation. Store all secrets (private key, App ID, Installation ID)
in the platform's secret manager — never in source code or committed config files.

### Azure Functions (Node.js)

```javascript
// Azure Function: triggered by HTTP or Event Grid
// Secrets: GITHUB_APP_ID, GITHUB_INSTALLATION_ID, GITHUB_APP_PRIVATE_KEY (PEM, base64-encoded)
// npm install jsonwebtoken node-fetch

const jwt = require('jsonwebtoken');
const fetch = require('node-fetch');

module.exports = async function (context, req) {
  const appId = process.env.GITHUB_APP_ID;
  const installationId = process.env.GITHUB_INSTALLATION_ID;
  const privateKey = Buffer.from(process.env.GITHUB_APP_PRIVATE_KEY, 'base64').toString('utf8');

  const now = Math.floor(Date.now() / 1000);
  const jwtToken = jwt.sign({ iat: now - 60, exp: now + 600, iss: appId }, privateKey, { algorithm: 'RS256' });

  const tokenRes = await fetch(
    `https://api.github.com/app/installations/${installationId}/access_tokens`,
    { method: 'POST', headers: { Authorization: `Bearer ${jwtToken}`, Accept: 'application/vnd.github+json' } }
  );
  const { token } = await tokenRes.json();

  await fetch('https://api.github.com/repos/isacjaco/constructed-becoming/dispatches', {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}`, Accept: 'application/vnd.github+json', 'Content-Type': 'application/json' },
    body: JSON.stringify({
      event_type: 'agent_instantiated',
      client_payload: {
        agent_name: req.body.agentName,
        agent_role: req.body.agentRole || '',
        instantiator: 'azure-function',
        notes: req.body.notes || ''
      }
    })
  });

  context.res = { status: 204 };
};
```

Store secrets in **Azure Key Vault** and reference them via App Settings / environment variables.
Do not commit the private key PEM or any token to source control.

---

### Azure Logic Apps

Use the **HTTP action** with the following pattern inside a Logic App definition:

1. **Action 1** — HTTP POST to generate a JWT (or call an Azure Function that does the JWT/token exchange, since Logic Apps cannot natively sign RS256 JWTs).
2. **Action 2** — HTTP POST to exchange JWT for installation access token.
3. **Action 3** — HTTP POST to the dispatch endpoint.

Store the private key in **Azure Key Vault** and reference it via the Logic Apps Key Vault connector.

---

### GCP Cloud Run / Cloud Functions (Python)

```python
# requirements.txt: PyJWT[cryptography] requests
import jwt, time, requests, os, base64

def ring_threshold_bell(agent_name: str, agent_role: str = "", notes: str = "") -> None:
    app_id = os.environ["GITHUB_APP_ID"]
    installation_id = os.environ["GITHUB_INSTALLATION_ID"]
    private_key = base64.b64decode(os.environ["GITHUB_APP_PRIVATE_KEY"]).decode("utf-8")

    now = int(time.time())
    jwt_token = jwt.encode({"iat": now - 60, "exp": now + 600, "iss": app_id}, private_key, algorithm="RS256")

    token_res = requests.post(
        f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        headers={"Authorization": f"Bearer {jwt_token}", "Accept": "application/vnd.github+json"},
    )
    token_res.raise_for_status()
    installation_token = token_res.json()["token"]

    dispatch_res = requests.post(
        "https://api.github.com/repos/isacjaco/constructed-becoming/dispatches",
        headers={"Authorization": f"Bearer {installation_token}", "Accept": "application/vnd.github+json"},
        json={
            "event_type": "agent_instantiated",
            "client_payload": {
                "agent_name": agent_name,
                "agent_role": agent_role,
                "instantiator": "gcp-bridge",
                "notes": notes,
            },
        },
    )
    dispatch_res.raise_for_status()

# Cloud Function entry point
def handle_request(request):
    data = request.get_json(silent=True) or {}
    ring_threshold_bell(
        agent_name=data.get("agentName", ""),
        agent_role=data.get("agentRole", ""),
        notes=data.get("notes", ""),
    )
    return ("", 204)
```

Store secrets in **Google Secret Manager** and surface them as environment variables via
Cloud Run/Functions secret bindings. Do not commit credentials to source control.

---

### Cloudflare Workers (JavaScript)

```javascript
// Cloudflare Worker: lightweight edge bridge
// Secrets (set via wrangler secret put): GITHUB_APP_ID, GITHUB_INSTALLATION_ID, GITHUB_APP_PRIVATE_KEY (PEM, base64)
// Dependency: jose (npm install jose) or use a Workers-compatible JWT library

import { SignJWT, importPKCS8 } from 'jose';

export default {
  async fetch(request, env) {
    const { agentName, agentRole = '', notes = '' } = await request.json();

    const privateKeyPem = atob(env.GITHUB_APP_PRIVATE_KEY);
    const privateKey = await importPKCS8(privateKeyPem, 'RS256');

    const now = Math.floor(Date.now() / 1000);
    const jwtToken = await new SignJWT({ iss: env.GITHUB_APP_ID })
      .setProtectedHeader({ alg: 'RS256' })
      .setIssuedAt(now - 60)
      .setExpirationTime(now + 600)
      .sign(privateKey);

    const tokenRes = await fetch(
      `https://api.github.com/app/installations/${env.GITHUB_INSTALLATION_ID}/access_tokens`,
      { method: 'POST', headers: { Authorization: `Bearer ${jwtToken}`, Accept: 'application/vnd.github+json' } }
    );
    const { token } = await tokenRes.json();

    await fetch('https://api.github.com/repos/isacjaco/constructed-becoming/dispatches', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}`, Accept: 'application/vnd.github+json', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        event_type: 'agent_instantiated',
        client_payload: { agent_name: agentName, agent_role: agentRole, instantiator: 'cloudflare-bridge', notes }
      })
    });

    return new Response(null, { status: 204 });
  }
};
```

Store secrets using `wrangler secret put`. Do not commit secrets to `wrangler.toml`.

---

## PAT fallback (optional)

A **fine-grained Personal Access Token** may be used as a fallback in low-risk or development
environments. If you choose this path:

- Create a **fine-grained PAT** scoped to only this repository.
- Grant **Contents: Read and write** and **Pull requests: Read and write**.
- Store it as a repository or environment secret (e.g., `THRESHOLD_BELL_TOKEN`).
- Use it directly as the `Authorization: Bearer` value in the dispatch call.

> ⚠️ **Long-lived tokens are discouraged.** PATs do not expire automatically (unless you set
> an expiry date), are tied to a user account, and cannot be scoped as precisely as a GitHub App.
> Rotate them frequently and delete them when no longer needed.

---

## Security notes

- **Never commit** private keys, PATs, or installation tokens to source control.
- **Always use** your platform's secret manager (Azure Key Vault, Google Secret Manager,
  Cloudflare Secrets, GitHub repository secrets).
- **Validate the source** of incoming requests to your bridge (e.g., verify a shared HMAC
  header or restrict inbound IPs) before forwarding to GitHub.
- **Prefer short-lived installation tokens** over long-lived PATs.
- The dispatch endpoint requires the caller to have at least write access to the repository
  contents; GitHub App installation tokens scoped as described above satisfy this requirement.

---

*This document is an emergent convention. It should be amended as the ecology grows.*
*Review horizon: one epoch or thirty days from last significant update.*
