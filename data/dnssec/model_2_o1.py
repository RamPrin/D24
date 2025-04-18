
from pytm import TM, Server, Dataflow, Datastore, Boundary, Actor

# Create the threat model object
tm = TM("DNSSEC Threat Model")

# Define boundaries
internet = Boundary("Internet")

# Define entities
dns_client = Actor("DNS Client")
dnssec_dns_server = Server("DNSSEC-Enabled DNS Server", inBoundary=internet)
dns_server = Server("Traditional DNS Server", inBoundary=internet)
zone_storage = Datastore("DNS Zone Storage", inBoundary=internet)

# Define data elements
dns_query = Dataflow(dns_client, dnssec_dns_server, "DNS Query", inBoundary=internet)
dns_response = Dataflow(dnssec_dns_server, dns_client, "DNS Response", inBoundary=internet)
zone_signing_keys = Dataflow(zone_storage, dnssec_dns_server, "Zone Signing Keys", inBoundary=internet)
key_signing_keys = Dataflow(zone_storage, dnssec_dns_server, "Key Signing Keys", inBoundary=internet)

# Define threats
dns_query.threat("Eavesdropping")
dns_response.threat("Tampering")
zone_signing_keys.threat("Key Compromise")
key_signing_keys.threat("Key Compromise")

# Add security properties
dns_query.data = {"Confidentiality": False, "Integrity": False}
dns_response.data = {"Confidentiality": False, "Integrity": True}
zone_signing_keys.data = {"Confidentiality": True, "Integrity": True}
key_signing_keys.data = {"Confidentiality": True, "Integrity": True}

# Process the threat model
tm.process()

# Print the threat model
tm.report()