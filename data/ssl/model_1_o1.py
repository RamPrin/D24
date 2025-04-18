from pytm import TM, Server, Client, Datastore, Dataflow, Boundary, Actor, Process

tm = TM()

# Define boundaries
internet = Boundary("Internet")
internal_network = Boundary("Internal Network")

# Define components
client = Actor("Client")
server = Server("Server")
certificate_authority = Datastore("Certificate Authority")

# Add components to boundaries
client.inBoundary = internet
server.inBoundary = internal_network
certificate_authority.inBoundary = internal_network

# Define dataflows
client_to_server = Dataflow(client, server, "ClientHello")
server_to_client_hello = Dataflow(server, client, "ServerHello")
server_to_client_certificate = Dataflow(server, client, "Certificate")
client_to_server_key_exchange = Dataflow(client, server, "ClientKeyExchange")
client_to_server_change_cipher_spec = Dataflow(client, server, "ChangeCipherSpec")
server_to_client_change_cipher_spec = Dataflow(server, client, "ChangeCipherSpec")
client_to_server_finished = Dataflow(client, server, "Finished")
server_to_client_finished = Dataflow(server, client, "Finished")

tm.process()