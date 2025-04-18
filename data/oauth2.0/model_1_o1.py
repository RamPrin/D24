
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