
from pytm import TM, Boundary, Actor, Server, Datastore, Dataflow

tm = TM("OAuth2 Authorization Code Flow Threat Model")

# Trust Boundaries
internet = Boundary("Internet")
internal = Boundary("Trust Boundary")

# Actors & Components
resource_owner = Actor("Resource Owner")
internet.add(resource_owner)

client_app = Server("Client Application")
internet.add(client_app)

auth_server = Server("Authorization Server")
internal.add(auth_server)

resource_server = Server("Resource Server")
internal.add(resource_server)

token_store = Datastore("Token Store")
auth_server.add(token_store)

# Dataflows
# 1. Authorization Code Request
df1 = Dataflow(resource_owner, client_app, "Auth Code Request")
df1.protocol = "HTTPS"
df1.method = "GET"
df1.url = "/authorize?response_type=code&client_id=..."

# 2. User Authentication & Consent
df2 = Dataflow(resource_owner, auth_server, "User Auth & Consent")
df2.protocol = "HTTPS"
df2.method = "POST"
df2.url = "/authorize (login & consent)"

# 3. Authorization Code Delivery (Redirect)
df3 = Dataflow(auth_server, client_app, "Authorization Code via Redirect")
df3.protocol = "HTTPS"

# 4. Access Token Request
df4 = Dataflow(client_app, auth_server, "Access Token Request")
df4.protocol = "HTTPS"
df4.method = "POST"
df4.url = "/token"

# 5. Access & Refresh Token Response
df5 = Dataflow(auth_server, client_app, "Access & Refresh Tokens")
df5.protocol = "HTTPS"

# 6. Persist Tokens
df6 = Dataflow(auth_server, token_store, "Persist Tokens")
df6.protocol = "local"

# 7. Protected Resource Request
df7 = Dataflow(client_app, resource_server, "API Request with Access Token")
df7.protocol = "HTTPS"
df7.method = "GET"
df7.header = "Authorization: Bearer <access_token>"

# 8. Token Validation
df8 = Dataflow(resource_server, auth_server, "Validate Access Token")
df8.protocol = "HTTPS"

tm.process()