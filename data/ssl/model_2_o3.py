
from pytm import TM, Boundary, Client, Server, Dataflow

class TLSHandshakeModel(TM):
    def __init__(self):
        super().__init__()
        self.name = "SSL/TLS Handshake Threat Model"
        # define trust zones
        bz_client = Boundary("ClientZone")
        bz_server = Boundary("ServerZone")
        # endpoints
        client = Client("Client")
        client.inBoundary = bz_client
        server = Server("Server")
        server.inBoundary = bz_server
        # TLS handshake data flows
        Dataflow(client, server, "ClientHello").protocol = "TLS 1.2"
        Dataflow(server, client, "ServerHello").protocol = "TLS 1.2"
        Dataflow(server, client, "Certificate").protocol = "TLS 1.2"
        Dataflow(client, server, "ClientKeyExchange").protocol = "TLS 1.2"
        Dataflow(client, server, "ChangeCipherSpec (C→S)").protocol = "TLS 1.2"
        Dataflow(client, server, "Finished (C→S)").protocol = "TLS 1.2"
        Dataflow(server, client, "ChangeCipherSpec (S→C)").protocol = "TLS 1.2"
        Dataflow(server, client, "Finished (S→C)").protocol = "TLS 1.2"

# instantiate to generate threats
model = TLSHandshakeModel()