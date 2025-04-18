
from pytm import TM, Actor, Process, Dataflow, Boundary, Element, Server

# Define a Threat Model
tm = TM("SSL/TLS Threat Model")

# Define boundaries
internet = Boundary("Internet")
enterprise_network = Boundary("Enterprise Network")

# Define entities
client = Actor("Client")
server = Server("Server")
certificate_authority = Actor("Certificate Authority")

# Define process elements
handshake_protocol = Process("SSL/TLS Handshake")
handshake_protocol.inBoundary = internet

certificate_verification = Process("Certificate Verification")
certificate_verification.inBoundary = internet

# Define data flows
df_client_to_server = Dataflow(client, server, "Client Hello")
df_client_to_server.protocol = "TLS 1.2"
df_client_to_server.data = "Version, Random, Cipher Suites, Compression Methods"
df_client_to_server.inBoundary = internet

df_server_to_client = Dataflow(server, client, "Server Hello & Certificate")
df_server_to_client.protocol = "TLS 1.2"
df_server_to_client.data = "Version, Random, Cipher Suite, Compression Method, Certificate"
df_server_to_client.inBoundary = internet

df_client_to_server_key_exchange = Dataflow(client, server, "Client Key Exchange")
df_client_to_server_key_exchange.protocol = "TLS 1.2"
df_client_to_server_key_exchange.data = "Encrypted Pre-Master Secret"
df_client_to_server_key_exchange.inBoundary = internet

df_change_cipher_spec = Dataflow(client, server, "Change Cipher Spec & Finished")
df_change_cipher_spec.protocol = "TLS 1.2"
df_change_cipher_spec.data = "Change Cipher Spec, Finished (Hash of messages)"
df_change_cipher_spec.inBoundary = internet

df_certificate_verification = Dataflow(certificate_authority, client, "Certificate Verification")
df_certificate_verification.protocol = "TLS 1.2"
df_certificate_verification.data = "CA's Public Key & Certificate Chain"
df_certificate_verification.inBoundary = internet

# Define the threats
client_to_server_threat = df_client_to_server.hasThreat(
    "Eavesdropping", "Transmission can be intercepted by attackers"
)
server_to_client_threat = df_server_to_client.hasThreat(
    "Tampering", "Messages can be altered by attackers"
)
server_cert_threat = df_certificate_verification.hasThreat(
    "Forged Certificate", "An attacker may use a fake certificate"
)

# Generate the report
tm.process()