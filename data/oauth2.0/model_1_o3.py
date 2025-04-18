
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