from pytm import TM, Server, Dataflow, Actor, Datastore, Boundary

tm = TM("OAuth 2.0 Authorization Code Flow")

user = Actor("Resource Owner")
client = Server("Client Application")
auth_server = Server("Authorization Server")
resource_server = Server("Resource Server")
client_db = Datastore("Client Database")
boundary = Boundary("Internet")

# User Authorization
user_to_client = Dataflow(user, client, "Request Access")
client_to_auth_server = Dataflow(client, auth_server, "Redirect User with Auth Request", ["code", "client_id", "redirect_uri", "scope", "state"])

# User Authentication and Authorization
auth_server_to_user = Dataflow(auth_server, user, "Authenticate and Authorize")
auth_server_to_client = Dataflow(auth_server, client, "Redirect with Authorization Code", ["code", "state"])

# Access Token Request
client_to_auth_server_token = Dataflow(client, auth_server, "Request Access Token", ["grant_type=authorization_code", "code", "redirect_uri", "client_id", "client_secret"])
client_to_auth_server_token.threats.append("Client credentials exposed")

# Access Token Response
auth_server_to_client_token = Dataflow(auth_server, client, "Access Token Response", ["access_token", "token_type", "expires_in", "scope"])

# Access Protected Resource
client_to_resource_server = Dataflow(client, resource_server, "Access Resource with Token", ["Authorization: Bearer access_token"])

# Resource Server Response
resource_server_to_client = Dataflow(resource_server, client, "Provide Requested Resource")

# Specify boundaries
user.inBoundary = boundary
client.inBoundary = boundary
auth_server.inBoundary = boundary
resource_server.inBoundary = boundary

tm.process()