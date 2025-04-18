Below is a list of identified threats against the Certificate Transparency system, organized by STRIDE. For each threat you’ll find a brief description and a DREAD assessment (scores 1–10; higher is worse), plus a total.

1. SPOOFING  
S1. Impersonate CA  +
 • Attacker masquerades as the Certificate Authority when issuing or delivering certs to clients.  
 D = 8, R = 6, E = 7, A = 10, D = 7 → Total 38  

S2. Impersonate CT Log Service +
 • Rogue service pretends to be an official CT log, feeding bogus STHs or proofs.  
 D = 7, R = 6, E = 7, A = 8, D = 7 → Total 35  

S3. Spoof Domain Owner  -
 • Attacker submits a counterfeit CSR under someone else’s domain to get a valid certificate.  
 D = 6, R = 7, E = 6, A = 5, D = 6 → Total 30  

S4. Spoof Client/Monitor/Auditor to CT Log +  
 • Unauthorized actor pretends to be a client/monitor/auditor to harvest proofs or logs.  
 D = 6, R = 8, E = 7, A = 5, D = 6 → Total 32  


2. TAMPERING  
T1. Tamper CSR in Transit  +
 • Attacker modifies the CSR between domain owner and CA, e.g. swapping public keys.  
 D = 4, R = 8, E = 8, A = 4, D = 7 → Total 31  

T2. Tamper raw_cert in CT Log Store  +
 • Modify or delete logged certificates before generating SCTs or STHs.  
 D = 7, R = 7, E = 6, A = 8, D = 7 → Total 35  

T3. Tamper SCT in Transit  +
 • Alter the Signed Certificate Timestamp en route from CT log to CA.  
 D = 7, R = 6, E = 7, A = 8, D = 7 → Total 35  

T4. Tamper Certificate+SCT to Client  +
 • Strip or modify the embedded SCT in the delivered certificate.  
 D = 8, R = 6, E = 7, A = 9, D = 7 → Total 37  

T5. Tamper STH/Inclusion Proof  -
 • Modify the Signed Tree Head or inclusion proof sent to client during validation.  
 D = 6, R = 7, E = 7, A = 7, D = 6 → Total 33  

T6. Tamper Alerts/Audit Reports  -
 • Modify or delete monitoring alerts or audit reports before they reach their destination.  
 D = 5, R = 6, E = 7, A = 5, D = 6 → Total 29  


3. REPUDIATION  
R1. CA Repudiates Issuance  +
 • CA later denies having issued a given certificate.  
 D = 5, R = 5, E = 5, A = 10, D = 5 → Total 30  

R2. CT Log Repudiates Logging  -
 • CT log claims it never recorded a specific certificate.  
 D = 5, R = 5, E = 5, A = 8, D = 5 → Total 28  

R3. Client Repudiates Validation  -
 • Client denies having performed validation or accepted a certificate.  
 D = 3, R = 6, E = 5, A = 7, D = 5 → Total 26  

R4. Monitor/Auditor Repudiates Action -  
 • Monitoring/audit service denies having raised an alert or issued a report.  
 D = 4, R = 5, E = 5, A = 5, D = 5 → Total 24  


4. INFORMATION DISCLOSURE  
I1. Eavesdrop CSR  +
 • Intercept CSRs to learn which domains are planning to deploy certificates.  
 D = 3, R = 9, E = 9, A = 4, D = 8 → Total 33  

I2. Eavesdrop raw_cert/SCT  +
 • Capture raw certificates or SCTs (though certs are public, SCT correlation may leak patterns).  
 D = 2, R = 9, E = 9, A = 3, D = 8 → Total 31  

I3. Unauthorized CT Log Store Access  -
 • Read or dump the entire CT log database.  
 D = 8, R = 6, E = 7, A = 10, D = 6 → Total 37  

I4. Leakage of Monitoring/Audit Data  -
 • Expose alerts or audit reports that may contain sensitive operational details.  
 D = 6, R = 7, E = 7, A = 8, D = 6 → Total 34  


5. DENIAL OF SERVICE  
D1. DDoS CT Log Service +
 • Prevent certificates from being logged or proofs from being served.  
 D = 7, R = 3, E = 6, A = 10, D = 6 → Total 32  

D2. DDoS CA Issuance Service  +
 • Block the CA’s ability to issue new certificates.  
 D = 8, R = 3, E = 6, A = 10, D = 6 → Total 33  

D3. DDoS Client Validation  +
 • Interrupt client requests for STHs or proofs, breaking certificate validation.  
 D = 5, R = 3, E = 6, A = 10, D = 6 → Total 30  

D4. DDoS Monitoring/Audit Infrastructure  +
 • Prevent alerts and audit reports from being generated or delivered.  
 D = 5, R = 3, E = 6, A = 7, D = 6 → Total 27  


6. ELEVATION OF PRIVILEGE  
E1. Compromise CT Log Admin  +
 • Attacker gains privileged access to add/remove entries in the CT log store.  
 D = 9, R = 4, E = 5, A = 10, D = 4 → Total 32  

E2. Compromise CA Admin  -
 • Attacker gains CA internals, issues arbitrary certificates for any domain.  
 D = 10, R = 4, E = 5, A = 10, D = 4 → Total 33  

E3. Escalation in Client/Monitor/Auditor  -
 • Attacker escalates privileges within client, monitor or auditor to tamper or spoof data.  
 D = 6, R = 5, E = 6, A = 7, D = 6 → Total 30  

---  
These cover the main threat vectors in the Certificate Transparency pipeline.