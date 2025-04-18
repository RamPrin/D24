
from pytm import TM, Boundary, Actor, Server, Store, Process, Dataflow

tm = TM("DNSSEC Threat Model")

# Boundaries
client_bw    = Boundary("Client Network")
resolver_bw  = Boundary("Resolver Environment")
server_bw    = Boundary("Authoritative Zone")

# Components
client       = Actor("Client", boundary=client_bw)
resolver     = Server("RecursiveResolver", boundary=resolver_bw)
auth_dns     = Server("AuthDNS", boundary=server_bw)
zonedb       = Store("ZoneDB", boundary=server_bw)
keystore     = Store("KeyStore", boundary=server_bw)
validation   = Process("Validation", boundary=client_bw)

# Dataflows
Dataflow(client,   resolver, "DNS Query",                                             protocols=["UDP/53"])
Dataflow(resolver, auth_dns, "DNSSEC Query",                                         protocols=["UDP/53"])
Dataflow(auth_dns, zonedb,   "Read Zone Data")
Dataflow(auth_dns, keystore, "Read ZSK/KSK")
Dataflow(auth_dns, resolver, "DNSSEC Response (RRs, RRSIGs, DNSKEYs)",                protocols=["UDP/53"])
Dataflow(resolver, client,   "DNSSEC Response (RRs, RRSIGs, DNSKEYs)",                protocols=["UDP/53"])
Dataflow(client,   validation, "Validate RRSIG and DNSKEY")

tm.process()