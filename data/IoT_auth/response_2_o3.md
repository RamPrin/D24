STRIDE – Threats and DREAD Ratings

1. Spoofing  
  S1. Spoof IoT Device  
    • Description: Attacker fakes a legitimate device’s identity (PSK/cert) to register and send malicious data.  
    D:7, R:5, E:6, A:6, D:6 → Total 30  

  S2. Spoof IoT Gateway  
    • Description: Attacker impersonates the gateway endpoint to intercept or reroute device messages.  
    D:8, R:4, E:6, A:8, D:5 → Total 31  

  S3. Spoof End‑User Credentials  
    • Description: Attacker steals or guesses user’s MFA or session tokens to access cloud service.  
    D:7, R:7, E:6, A:9, D:7 → Total 36  

  S4. Spoof Administrator (SSH Hijack)  
    • Description: Attacker steals or replays SSH keys/passwords to gain privileged access on auth server.  
    D:9, R:4, E:5, A:3, D:6 → Total 27  

2. Tampering  
  T1. Tamper Registration Data  
    • Description: Modify MQTT/TLS registration payload to inject rogue configuration or commands.  
    D:6, R:7, E:7, A:6, D:6 → Total 32  

  T2. Tamper OAuth2 Auth Request  
    • Description: Alter OAuth2 parameters in transit to escalate privileges or redirect tokens.  
    D:8, R:6, E:6, A:7, D:6 → Total 33  

  T3. Tamper JWT/Token in Transit  
    • Description: Modify or strip claims from returned token/JWT to bypass authorization checks.  
    D:7, R:6, E:7, A:8, D:6 → Total 34  

  T4. Tamper Session Store Entries  
    • Description: Modify encrypted session records in the credential store to hijack sessions.  
    D:7, R:5, E:6, A:7, D:5 → Total 30  

3. Repudiation  
  R1. Inadequate Device‑Registration Logging  
    • Description: Lack of tamper‑proof logs allows devices (or attackers) to deny having registered.  
    D:5, R:8, E:5, A:4, D:7 → Total 29  

  R2. User Transaction Denial  
    • Description: End users deny having performed sensitive operations (e.g. configuration changes).  
    D:6, R:7, E:5, A:8, D:7 → Total 33  

  R3. Admin Config‑Change Denial  
    • Description: Administrator denies having applied critical auth‑server configuration changes.  
    D:8, R:6, E:7, A:3, D:6 → Total 30  

4. Information Disclosure  
  I1. Eavesdrop MQTT Credentials  
    • Description: Passive attacker intercepts PSK or certificate exchange during device registration.  
    D:7, R:8, E:7, A:7, D:8 → Total 37  

  I2. Eavesdrop OAuth2/TLS Credentials  
    • Description: MITM attack decrypts or downgrades TLS to capture OAuth2 client secrets.  
    D:8, R:7, E:6, A:8, D:7 → Total 36  

  I3. Credential‑Store Leakage  
    • Description: Unauthorized read of user/device credentials or salts from internal datastore.  
    D:9, R:3, E:4, A:9, D:3 → Total 28  

  I4. Sniff Auth‑Response Tokens  
    • Description: Intercept JWTs or tokens returned to gateway, then replay or analyze claims.  
    D:8, R:6, E:7, A:8, D:7 → Total 36  

  I5. Session‑Store Data Exposure  
    • Description: Read unencrypted or poorly encrypted session state in cloud service datastore.  
    D:8, R:6, E:6, A:8, D:6 → Total 34  

5. Denial of Service  
  D1. Gateway Flood (MQTT Connection Spam)  
    • Description: Flood gateway with fake registration or data messages to exhaust resources.  
    D:6, R:8, E:8, A:8, D:9 → Total 39  

  D2. Auth‑Server Flood (OAuth Requests)  
    • Description: Overwhelm auth server with token requests, causing legitimate requests to fail.  
    D:8, R:7, E:8, A:9, D:9 → Total 41  

  D3. SSH Brute‑Force on Auth Server  
    • Description: Repeated SSH login attempts lock out admin or consume server CPU.  
    D:7, R:7, E:8, A:5, D:7 → Total 34  

  D4. Cloud Service Outage via Session‑Store Queries  
    • Description: Excessive read/write operations against session store degrade or crash service.  
    D:9, R:5, E:6, A:9, D:6 → Total 35  

6. Elevation of Privilege  
  E1. Stolen Token Replay  
    • Description: Reuse intercepted JWT/token to access higher‑privilege endpoints on gateway/cloud.  
    D:8, R:6, E:7, A:9, D:7 → Total 37  

  E2. SQL Injection on Credential Store  
    • Description: Exploit improper input sanitization in credential‑verify queries to gain admin.  
    D:9, R:4, E:5, A:9, D:4 → Total 31  

  E3. MFA Bypass on Cloud Service  
    • Description: Social‑engineering or technical bypass of second factor to assume user identity.  
    D:9, R:3, E:4, A:9, D:3 → Total 28  

  E4. Admin SSH Exploit  
    • Description: Exploit vulnerable SSH server or library to execute arbitrary code as root.  
    D:9, R:2, E:3, A:4, D:2 → Total 20