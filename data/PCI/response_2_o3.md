STRIDE: Spoofing  
1. Spoofing User Session  
  Description: Attacker steals or forges cardholder credentials or session tokens to transact under a victim’s identity.  
  DREAD: D 8, R 7, E 6, A 8, D 7 → Total 36, Avg 7.2  

2. Impersonate QSA  
  Description: Attacker poses as the QSA/Assessor to gain privileged access or extract assessment data.  
  DREAD: D 7, R 5, E 5, A 6, D 4 → Total 27, Avg 5.4  

3. DNS/TLS Certificate Spoofing (MITM)  
  Description: Attacker poisons DNS or issues a fake TLS cert to intercept or redirect cardholder traffic.  
  DREAD: D 8, R 5, E 5, A 7, D 6 → Total 31, Avg 6.2  

STRIDE: Tampering  
4. TLS Downgrade Attack  
  Description: Forcing a fall‑back to weaker cipher suites so that PAN in transit can be altered.  
  DREAD: D 7, R 6, E 7, A 6, D 5 → Total 31, Avg 6.2  

5. SQL Injection  
  Description: Malicious SQL payloads injected via the web app to read or modify the cardholder database.  
  DREAD: D 9, R 8, E 8, A 9, D 7 → Total 41, Avg 8.2  

6. Audit Log Tampering  
  Description: Attacker modifies or deletes entries in the Audit Log Store to cover tracks.  
  DREAD: D 6, R 7, E 7, A 5, D 5 → Total 30, Avg 6.0  

STRIDE: Repudiation  
7. Transaction Non‑Repudiation Gap  
  Description: Inadequate logging allows a cardholder to deny a valid transaction.  
  DREAD: D 5, R 4, E 4, A 6, D 3 → Total 22, Avg 4.4  

8. Admin Action Denial  
  Description: Attacker erases or alters admin‑level logs so unauthorized changes can’t be traced.  
  DREAD: D 6, R 5, E 5, A 6, D 4 → Total 26, Avg 5.2  

STRIDE: Information Disclosure  
9. PAN Data Leakage  
  Description: Exposure of encrypted or unencrypted PANs via backup misconfiguration or DB vulnerability.  
  DREAD: D 9, R 7, E 7, A 9, D 8 → Total 40, Avg 8.0  

10. Sensitive Data in Logs  
  Description: PAN fragments or other cardholder data logged in cleartext in the Audit Log Store.  
  DREAD: D 8, R 7, E 6, A 8, D 7 → Total 36, Avg 7.2  

STRIDE: Denial of Service  
11. Application‑Layer DoS  
  Description: Flooding the web application with HTTP requests to exhaust resources and deny service.  
  DREAD: D 7, R 8, E 8, A 7, D 8 → Total 38, Avg 7.6  

12. Brute‑Force DB Access / Lockout  
  Description: Repeated login attempts against the database to exhaust authentication throttles or lock accounts.  
  DREAD: D 6, R 7, E 7, A 6, D 6 → Total 32, Avg 6.4  

13. Log Store Exhaustion  
  Description: Generating excessive transactions to fill or corrupt the Audit Log Store, preventing future writes.  
  DREAD: D 5, R 7, E 7, A 6, D 6 → Total 31, Avg 6.2  

STRIDE: Elevation of Privilege  
14. Web App Privilege Escalation  
  Description: Exploiting a flaw in the web application to execute code or commands at higher privileges.  
  DREAD: D 9, R 7, E 6, A 9, D 6 → Total 37, Avg 7.4  

15. Firewall Rule Bypass  
  Description: Misconfiguring or exploiting the firewall to gain direct access to the CDE’s internal systems.  
  DREAD: D 8, R 6, E 6, A 8, D 5 → Total 33, Avg 6.6