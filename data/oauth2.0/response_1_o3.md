# Model:
```python
from pytm import TM, Boundary, Server, Client, DataStore, DataFlow, ExternalEntity

tm = TM("OAuth 2.0 Authorization Code Flow")

# Boundaries
internet = Boundary("Internet Boundary")
client_boundary = Boundary("Client Boundary")
auth_boundary = Boundary("Authorization Server Boundary")
resource_boundary = Boundary("Resource Server Boundary")

# Components
user = ExternalEntity("User", boundary=internet)
client = Client("Client Application", boundary=client_boundary)
auth_server = Server("Authorization Server", boundary=auth_boundary)
resource_server = Server("Resource Server", boundary=resource_boundary)
token_store = DataStore("Token Store", boundary=auth_boundary)
resource_db = DataStore("Resource DB", boundary=resource_boundary)

# Dataflows
DataFlow(user, client, "Initiate Authorization Request", boundary0=internet, boundary1=client_boundary)
DataFlow(client, auth_server, "GET /authorize?response_type=code&client_id&redirect_uri&scope&state", boundary0=client_boundary, boundary1=auth_boundary)
DataFlow(auth_server, user, "Login Page & Consent", boundary0=auth_boundary, boundary1=internet)
DataFlow(user, auth_server, "Submit Credentials & Consent", boundary0=internet, boundary1=auth_boundary)
DataFlow(auth_server, client, "Redirect with Authorization Code (code & state)", boundary0=auth_boundary, boundary1=client_boundary)
DataFlow(client, auth_server, "POST /token (grant_type=authorization_code, code, client_id, client_secret)", boundary0=client_boundary, boundary1=auth_boundary)
DataFlow(auth_server, client, "Access Token Response (access_token, refresh_token)", boundary0=auth_boundary, boundary1=client_boundary)
DataFlow(auth_server, token_store, "Store Refresh Token", boundary0=auth_boundary, boundary1=auth_boundary)
DataFlow(client, resource_server, "GET /resource Authorization: Bearer access_token", boundary0=client_boundary, boundary1=resource_boundary)
DataFlow(resource_server, resource_db, "Read Protected Resource", boundary0=resource_boundary, boundary1=resource_boundary)
DataFlow(resource_server, client, "Return Protected Resource", boundary0=resource_boundary, boundary1=client_boundary)

tm.process()
```

# Threats
Spoofing:
- Client Impersonation: An attacker registers or spoofs a legitimate client_id to receive authorization codes and tokens.
- Resource Owner Impersonation: Attacker steals or guesses user credentials at the authorization server login.
- Authorization Server Spoofing: Fake auth server captures credentials and authorization codes via malicious redirect.
- Resource Server Spoofing: Malicious endpoint impersonates the resource server to capture bearer tokens.
- User Agent Spoofing: An attacker forges browser headers or User-Agent to bypass client‑side checks.

Tampering:
- Authorization Code Tampering: Modify the code parameter in the redirect URI to intercept or misroute authorization.
- State Parameter Tampering: Alter or remove the state value to perform CSRF or hijack the callback.
- Access Token Modification: Intercept and modify bearer tokens in transit to gain unauthorized access.
- Request Parameter Tampering: Change grant_type, redirect_uri or scope parameters to bypass server validation.
- Token Store Tampering: Unauthorized modification or deletion of tokens in the authorization server’s datastore.

Repudiation:
- Missing Audit Logs: Lack of detailed logs at the auth or resource servers prevents proving who requested or used tokens.
- Consent Repudiation: User or client denies having granted consent; no signed proof prevents dispute resolution.
- Code Exchange Repudiation: Client denies having exchanged the authorization code for tokens; absence of proof hinders accountability.
- Token Usage Repudiation: Resource server lacks logging of which token accessed which resource and when.

Information Disclosure:
- Authorization Code in URL: Codes in query parameters can leak via browser history, referrer logs, or proxy logs.
- Access Token Leakage via Referrer: Misconfigured endpoints include bearer tokens in referrer headers.
- Client Secret Exposure: Insecure storage or transmission of client_secret in client‑side apps or logs.
- Insecure Transport (HTTP): Credentials, codes, and tokens exposed in plaintext if HTTPS is not enforced.
- Token Storage Leakage: Insecure token storage on client devices (e.g., localStorage) allows local attackers to steal them.

Denial of Service:
- Authorization Endpoint Flooding: High volumes of /authorize requests exhaust auth server resources or trigger rate limits.
- Token Endpoint Abuse: Repeated invalid token exchange attempts consume CPU and database I/O at the auth server.
- Resource Server Overload: Flooding resource requests (with valid or invalid tokens) exhausts server or database.
- Code Replay Lockout: Replaying valid authorization codes triggers repeated validation and may lock out legitimate flows.

Elevation of Privilege:
- Scope Manipulation: Attacker requests extra scopes in /authorize and the server fails to validate against registered scopes.
- Refresh Token Abuse: Stolen refresh tokens used to obtain long‑lived access tokens and access unauthorized resources.
- Open Redirect Exploitation: Malicious actors exploit weak redirect_uri validation to escalate privileges or phish tokens.
- Token Forgery via Weak Signing: Exploit weak or absent signature algorithms to craft tokens with elevated privileges.