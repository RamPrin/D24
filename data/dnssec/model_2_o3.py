
from pytm import TM, Actor, Server, DataStore, Process, Boundary, Dataflow

tm = TM("DNSSEC Threat Model")

# Trust Boundaries
internet = Boundary("Internet")
zone_authority = Boundary("Zone Authority")
key_storage = Boundary("Key Storage")

# Actors and Systems
client = Actor("DNS Client", boundary=internet)
dns_server = Server("DNSSEC DNS Server", boundary=internet)
zone_admin = Actor("Zone Administrator", boundary=zone_authority)
attacker = Actor("Attacker", boundary=internet)

# Data Stores
ksk_priv = DataStore("KSK Private Key", boundary=key_storage)
zsk_priv = DataStore("ZSK Private Key", boundary=key_storage)
dns_zone = DataStore("DNS Zone Records", boundary=zone_authority)
dnskey_pub = DataStore("Published DNSKEY Records", boundary=internet)

# Processes
key_generation = Process("Key Generation", boundary=zone_authority)
record_signing = Process("Record Signing", boundary=zone_authority)
key_publication = Process("Key Publication", boundary=zone_authority)
query_handling = Process("Query Handling", boundary=internet)
signature_verification = Process("Signature Verification", boundary=internet)

# Data Flows
Dataflow(zone_admin, key_generation, "Generate KSK & ZSK")
Dataflow(key_generation, ksk_priv, "Store KSK")
Dataflow(key_generation, zsk_priv, "Store ZSK")

Dataflow(zone_admin, record_signing, "Zone data & ZSK", data=[dns_zone, zsk_priv])
Dataflow(record_signing, dns_zone, "Signed RRsets", data=[dns_zone])

Dataflow(zone_admin, key_publication, "Publish DNSKEYs (ZSK,KSK)", data=[dnskey_pub, ksk_priv])

Dataflow(client, query_handling, "DNS query")
Dataflow(query_handling, dns_server, "Forward query")
Dataflow(dns_server, query_handling, "DNSSEC response (RRsets+RRSIGs+DNSKEYs)", data=[dns_zone, dnskey_pub])
Dataflow(query_handling, client, "Response + signatures", data=[dnskey_pub])

Dataflow(client, signature_verification, "Verify RRSIGs with DNSKEYs", data=[dnskey_pub])

# Attacker can spoof or tamper on the public network
Dataflow(attacker, client, "MITM: spoofed or tampered DNS response")

tm.process()