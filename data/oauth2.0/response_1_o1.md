# Model:
```python
from pytm import TM, Server, Dataflow, Boundary, Actor

# Define boundaries
internet_boundary = Boundary("Internet")
internal_boundary = Boundary("Internal Network")

# Define components
authorization_server = Server("Authorization Server")
resource_server = Server("Resource Server")
client_application = Server("Client Application")
resource_owner = Actor("Resource Owner")

# Define dataflows
Dataflow(resource_owner, authorization_server, "User Authorization Request")
Dataflow(authorization_server, resource_owner, "Authorization Code Redirect", data_classification="Confidential")
Dataflow(client_application, authorization_server, "Access Token Request", data_classification="Sensitive")
Dataflow(authorization_server, client_application, "Access Token Response", data_classification="Sensitive")
Dataflow(client_application, resource_server, "Resource Request with Access Token", data_classification="Sensitive")
Dataflow(resource_server, client_application, "Resource Response")

tm = TM("OAuth 2.0 Authorization Code Flow")
tm += [internet_boundary, internal_boundary, authorization_server, resource_server, client_application, resource_owner]

tm.process()
```

# Threats

Spoofing:
- Authorization Server Impersonation: An attacker could set up a rogue authorization server to impersonate the legitimate one, tricking the client or resource owner. -
- Client Impersonation: An attacker could impersonate a client application to obtain unauthorized access tokens. +

Tampering:
- Token Tampering: An attacker intercepts and alters an access token to gain unauthorized access to resources. +
- Dataflow Manipulation: Modifying data inflow to the authorization server to alter the authorization process. -

Repudiation:
- Lack of Logging: Without proper logging, users might deny having performed specific authorization actions. -
- State Manipulation: An attacker could modify or reuse the state parameter to evade tracking and auditing. +

Information Disclosure:
- Access Token Leak via URL: If access tokens are transferred in URLs, they may be exposed to third parties through referrer headers. +
- Client Secret Exposure: Client secrets stored insecurely could be disclosed and used by unauthorized parties. +

Denial of Service (DoS):
- Excessive Authorization Requests: Repeated unauthorized requests could flood the authorization server, potentially causing service denial. +
- Token Flooding: An attacker might flood the authorization server with token requests to exhaust resources. +

Elevation of Privilege:
- Privilege Escalation via Misconfigured Resource Server: Misconfigurations might allow access tokens to grant more privileges than intended. - 
- Improper Scope Handling: An attacker could exploit improper scope handling to gain broader access than permitted. +