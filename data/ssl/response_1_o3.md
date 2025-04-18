# Model:
```python
from pytm import TM, Boundary, Client, Server, Dataflow

# Threat model for SSL/TLS handshake
tm = TM("SSL/TLS Handshake Protocol")

# Boundaries
internet = Boundary("Internet")

# Components
client = Client("Client")
server = Server("Server")

internet.add(client, server)

# Dataflows (handshake messages)
Dataflow(client, server, "ClientHello")
Dataflow(server, client, "ServerHello")
Dataflow(server, client, "Certificate")
Dataflow(server, client, "ServerKeyExchange")
Dataflow(server, client, "ServerHelloDone")
Dataflow(client, server, "ClientKeyExchange")
Dataflow(client, server, "ChangeCipherSpec (Client)")
Dataflow(client, server, "Finished (Client)")
Dataflow(server, client, "ChangeCipherSpec (Server)")
Dataflow(server, client, "Finished (Server)")

tm.process()
```

# Threats
Spoofing:
- Server Impersonation: Attacker presents a forged certificate to the client to impersonate the server.
- Client Impersonation: Attacker masquerades as a legitimate client to gain unauthorized access to the server.
- MITM Handshake Relay: Attacker positions between client and server, relaying and modifying handshake messages.

Tampering:
- Cipher Suite Downgrade: Attacker removes strong cipher suites from ClientHello to force weaker encryption.
- Handshake Message Modification: Attacker alters ServerHello or Certificate messages to break authentication.
- Finished Message Tampering: Attacker modifies the Finished message hashes to disrupt handshake integrity.

Repudiation:
- Handshake Non‑Repudiation Absence: No reliable logging of handshake steps allows parties to deny having initiated a session.
- Silent Certificate Acceptance: Client suppresses certificate errors without logging, enabling denial of acceptance of invalid certs.
- Unlogged Renegotiation: Lack of audit trails for TLS renegotiation permits denial of unexpected or malicious renegotiation.

Information Disclosure:
- Handshake Sniffing: Passive attacker captures handshake messages, learning protocol versions, cipher suites, and random nonces.
- Certificate Chain Exposure: Intercepted Certificate flow reveals internal hostnames or infrastructure details.
- Session Ticket Leakage: Attacker intercepts session resumption tickets, enabling later session hijacking.
- Pre‑master Secret Exposure: Weak RSA padding or implementation bugs leak the pre‑master secret to eavesdroppers.

Denial of Service:
- Handshake Flood: Attacker sends a high volume of ClientHello messages to exhaust server CPU and memory.
- Expensive Key Exchange DoS: Forcing many ECDHE/DH handshakes to deplete server computational resources.
- Fragmentation Attack: Malformed or overly fragmented handshake messages consume excessive memory buffers.

Elevation of Privilege:
- Protocol Downgrade (POODLE): Attacker forces fallback to SSLv3 to exploit known SSLv3 vulnerabilities.
- NULL Cipher Injection: Attacker injects a null‑encryption cipher suite to disable confidentiality.
- Weak Key Attack (Logjam): Forcing use of weak (e.g., 512‑bit) DH parameters to break key exchange and derive the master secret.
- Deprecated Hash Algorithm Downgrade: Attacker enforces use of MD5/SHA‑1 for Finished message, enabling collision attacks.
