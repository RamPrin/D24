Below is a list of identified threats against the IoT‑Supply‑Chain system, organized by STRIDE category. Each threat has a brief description and a DREAD score (sum of Damage, Reproducibility, Exploitability, Affected Users, Discoverability; each rated 1–10, total out of 50).

1. SPOOFING
 1.1 Sensor Identity Spoofing  
    – Attacker injects fake sensor readings by impersonating legitimate IoT sensors.  
    DREAD = D7/R8/E6/A8/D7 = 36  
 1.2 Gateway Impersonation  
    – Attacker pretends to be the EdgeGateway to send malicious or altered data upstream.  
    DREAD = 8/6/5/7/6 = 32  
 1.3 User Credential Theft  
    – Attacker steals or guesses SupplyChainUser credentials to access SCMSystem.  
    DREAD = 7/7/7/9/8 = 38  

2. TAMPERING
 2.1 Firmware Tampering on Devices  
    – Malicious firmware is installed on sensors or gateways to alter behavior.  
    DREAD = 8/7/4/6/6 = 31  
 2.2 Data-in‑Transit Modification  
    – Attacker intercepts and alters data flows (e.g. edge→analytics) despite TLS.  
    DREAD = 7/8/6/8/5 = 34  
 2.3 Data-at‑Rest Tampering  
    – Attacker gains write access to DataStorage or SCM DB and corrupts records.  
    DREAD = 8/6/5/7/5 = 31  

3. REPUDIATION
 3.1 Log Forgery  
    – Attacker or malicious insider alters or deletes audit logs in cloud services.  
    DREAD = 6/5/5/7/6 = 29  
 3.2 Shipment Instruction Denial  
    – User or attacker denies having sent a shipping order to SCMSystem; lack of non‑repudiation.  
    DREAD = 7/4/4/7/5 = 27  

4. INFORMATION DISCLOSURE
 4.1 Wireless Eavesdropping  
    – Sniffing unencrypted wireless traffic between sensors and gateway.  
    DREAD = 6/8/5/9/7 = 35  
 4.2 TLS MITM Attack  
    – Attacker intercepts/decodes supposedly encrypted TLS flows (e.g. User→SCM).  
    DREAD = 7/7/6/8/6 = 34  
 4.3 Cloud Data Leakage  
    – Misconfiguration or insider leads to exposure of Inventory, Transportation, Warehouse data.  
    DREAD = 9/6/7/8/4 = 34  
 4.4 Insider Data Exfiltration  
    – Authorized admin or dev steals sensitive supply‑chain records from SCM or IMS.  
    DREAD = 8/5/6/7/4 = 30  

5. DENIAL OF SERVICE
 5.1 Wireless Jamming  
    – RF interference disrupts sensor→gateway communications.  
    DREAD = 6/7/6/9/6 = 34  
 5.2 Edge Gateway DoS  
    – Flooding or resource exhaustion attack against the EdgeGateway.  
    DREAD = 7/6/5/8/5 = 31  
 5.3 Cloud Service Overload  
    – Bot‑driven or burst load saturates DataAnalytics, SCMSystem or WMS, halting operations.  
    DREAD = 8/5/4/8/4 = 29  

6. ELEVATION OF PRIVILEGE
 6.1 Edge Gateway Root Escalation  
    – Exploiting a vulnerability on the gateway OS to gain root and control all connected devices.  
    DREAD = 8/5/5/7/5 = 30  
 6.2 Cloud Admin Privilege Escalation  
    – Gaining higher‑level privileges in the cloud platform to tamper with any service (DataStorage, SCM, etc.).  
    DREAD = 9/6/4/8/6 = 33  

Total threats identified: 16  