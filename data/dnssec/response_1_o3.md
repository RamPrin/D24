# Model:
```python
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
```

# Threats
Spoofing:
- Forged DNS Response: Attacker sends spoofed DNSSEC response claiming to be from AuthDNS. +
- Fake DNSKEY Injection: Attacker injects a malicious DNSKEY record to bypass signature checks. +
- Spoofed NSEC/NSEC3 Record: Attacker forges authenticated denial of existence to hide or fake records.-
- Resolver Impersonation: Attacker pretends to be the resolver to intercept client queries. -

Tampering:
- In-Transit DNS Record Modification: Attacker alters DNS record data or signatures as they travel. +
- Zone File Tampering: Insider or attacker modifies zone data in ZoneDB to redirect domains. +
- Private Key Tampering: Attacker replaces or corrupts ZSK/KSK in KeyStore to break signature trust. -
- RRSIG Record Tampering: Attacker modifies RRSIG values in responses to cause verification failures. +

Repudiation:
- Lack of Audit Logging: No immutable logs at AuthDNS or resolver allow denial of signing actions. -
- Log Tampering: Attacker or insider alters DNSSEC operation logs to erase trace of malicious changes. -
- Client Query Denial: Client repudiates having sent or received specific DNS queries without proof. +
- Resolver Response Denial: Resolver denies having served or cached specific DNSSEC responses. -

Information Disclosure:
- DNS Query Eavesdropping: Passive attacker captures client queries, exposing browsing behavior. +
- Zone Transfer Leakage: Unauthorized AXFR exposes entire zone contents, revealing private hostnames. +
- KeyStore Data Breach: Compromise of KeyStore leaks private ZSK/KSK, allowing signature forgeries. +
- DNS Cache Snooping: Attacker infers resolver cache contents and client activity by timing attacks. -

Denial of Service:
- DNSSEC Amplification Attack: Large signed responses used in UDP reflection floods. +
- Signature Computation Exhaustion: Flood of signature requests overwhelms AuthDNS CPU. +
- UDP Flooding on Port 53: Volumetric attack against resolver or AuthDNS to disrupt DNS service. +
- Chain-of-Trust Disruption: Attacker blocks DNSKEY or DS delivery, causing resolver validation failures. -

Elevation of Privilege:
- Unauthorized Zone Transfer: Attacker abuses AXFR to steal zone and craft malicious responses. +
- KSK Rollover Abuse: Attacker injects rogue KSK during rollover to gain signing authority. -
- TSIG/Dynamic Update Exploit: Attacker uses misconfigured TSIG keys to inject unauthorized records. +
- Resolver Cache Poisoning: Attacker injects forged records into resolver cache to redirect clients. +