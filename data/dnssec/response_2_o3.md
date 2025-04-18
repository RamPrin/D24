STRIDE Category: Spoofing  
1. DNS Server Impersonation  +
   Description: Attacker spoofs DNSSEC server responses to return malicious records.  
   DREAD – D:8, R:7, E:8, A:9, D:8 → Score 40  
2. Zone Authority Impersonation +  
   Description: Attacker masquerades as zone administrator to publish fraudulent DNSKEYs.  
   DREAD – D:9, R:6, E:7, A:5, D:7 → Score 34  

STRIDE Category: Tampering  
3. DNS Response Tampering  +
   Description: MITM modifies RRsets or RRSIGs in transit to mislead the client.  
   DREAD – D:8, R:7, E:7, A:8, D:8 → Score 38  
4. DNSKEY Publication Alteration  +
   Description: Attacker intercepts and alters the published DNSKEY records.  
   DREAD – D:9, R:6, E:6, A:7, D:7 → Score 35  
5. Zone Data Tampering at Rest  -
   Description: Unauthorized modification of DNS zone records in the zone-authority store.  
   DREAD – D:8, R:5, E:6, A:4, D:5 → Score 28  
6. Key Material Tampering  -
   Description: Modification of private keys (ZSK/KSK) within key storage.  
   DREAD – D:10, R:4, E:5, A:3, D:4 → Score 26  

STRIDE Category: Repudiation  
7. Signature Denial by Zone Admin +  
   Description: Zone administrator denies having signed a set of records.  
   DREAD – D:4, R:6, E:5, A:2, D:5 → Score 22  
8. Client Denies Receipt of Responses -  
   Description: Client repudiates having received (or verified) DNSSEC responses.  
   DREAD – D:3, R:6, E:5, A:3, D:6 → Score 23  

STRIDE Category: Information Disclosure  
9. KSK Private Key Leakage  +
   Description: Compromise or leakage of the KSK undermines the trust chain.  
   DREAD – D:10, R:3, E:4, A:9, D:3 → Score 29  
10. ZSK Private Key Leakage  -
    Description: Exposure of the ZSK allows forging of valid RRSIGs for the zone.  
    DREAD – D:9, R:4, E:5, A:8, D:4 → Score 30  
11. DNS Zone Data Exposure  +
    Description: Unauthorized reading of unpublished zone records reveals internal mappings.  
    DREAD – D:6, R:5, E:6, A:4, D:5 → Score 26  
12. DNS Query Eavesdropping  +
    Description: Attacker intercepts client queries, leaking browsing or service patterns.  
    DREAD – D:5, R:8, E:8, A:8, D:8 → Score 37  

STRIDE Category: Denial of Service  
13. DNS Query Flooding  +
    Description: Overwhelm the DNSSEC server with queries to disrupt service.  
    DREAD – D:7, R:9, E:8, A:8, D:8 → Score 40  
14. Signing Process Exhaustion +  
    Description: Flood the record-signing process to delay or halt zone updates.  
    DREAD – D:5, R:6, E:7, A:4, D:7 → Score 29  
15. Key Generation Disruption  -
    Description: Interrupt or overload key generation to prevent key rotation.  
    DREAD – D:4, R:5, E:6, A:3, D:6 → Score 24  

STRIDE Category: Elevation of Privilege  
16. Key Storage Compromise  +
    Description: Attacker gains write access to key-storage boundary and injects malicious keys.  
    DREAD – D:10, R:4, E:5, A:3, D:4 → Score 26  
17. Zone Authority Server Exploit -  
    Description: Vulnerability on the zone-authority machine is exploited for full control.  
    DREAD – D:9, R:5, E:5, A:6, D:6 → Score 31  
18. DNS Server Privilege Escalation -  
    Description: Attacker exploits DNS server software to gain administrative privileges.  
    DREAD – D:7, R:5, E:6, A:7, D:6 → Score 31