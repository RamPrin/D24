
from pytm import TM, Server, Actor, Dataflow, datastore, Boundary, Process

# Define Trust Boundaries
internet = Boundary("Internet")
client_boundary = Boundary("Client Boundary")
auth_server_boundary = Boundary("Authorization Server Boundary")
resource_server_boundary = Boundary("Resource Server Boundary")

# Define Actors
user = Actor("Resource Owner", boundary=internet)

# Define Processes
client_app = Process("Client", boundary=client_boundary)
auth_server = Server("Authorization Server", boundary=auth_server_boundary)
resource_server = Server("Resource Server", boundary=resource_server_boundary)

# Define Data Flows
auth_request = Dataflow(user, auth_server, "Authorization Request").inBoundary(internet)
auth_code_flow = Dataflow(auth_server, client_app, "Authorization Code").inBoundary(internet)
token_request = Dataflow(client_app, auth_server, "Access Token Request").inBoundary(internet)
token_response = Dataflow(auth_server, client_app, "Access Token Response").inBoundary(internet)
resource_request = Dataflow(client_app, resource_server, "Protected Resource Request", "Bearer token")
resource_response = Dataflow(resource_server, client_app, "Protected Resource Response")

# Define Data Store
token_datastore = datastore("Token Storage", boundary=auth_server_boundary)

# Define the Threat Model
tm = TM("OAuth 2.0 Authorization Protocol")

# Threats Considerations
tm.process()

# Save or visualize your model as needed