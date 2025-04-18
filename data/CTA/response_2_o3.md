STRIDE: Spoofing  
1. Spoofing User Identity  
  An attacker impersonates a legitimate user’s credentials to register or query exposure data. +
  DREAD – D:6, R:5, E:5, A:6, D:5 (Total 27)

2. Spoofing Bluetooth Interface  
  A rogue device broadcasts fabricated UUIDs to pollute contact logs or track users. -
  DREAD – D:4, R:7, E:6, A:7, D:7 (Total 31)

3. Spoofing Health Authority  
  An attacker masquerades as the HealthAuthority to request or inject aggregate data. + 
  DREAD – D:7, R:4, E:5, A:8, D:4 (Total 28)

STRIDE: Tampering  
4. Tampering with UUID Broadcast  +
  Altering the UUIDs emitted by the BLEInterface to mislead exposure calculations.  
  DREAD – D:5, R:7, E:6, A:8, D:6 (Total 32)

5. Tampering with GPS Data  +
  User or malware modifies GPSInterface data before upload to falsify location logs.  
  DREAD – D:5, R:7, E:7, A:8, D:6 (Total 33)

6. Tampering with Data in Transit (MITM) + 
  Intercepting and altering TLS-encrypted traffic between MobileApp and BackendServer.  
  DREAD – D:7, R:6, E:6, A:9, D:5 (Total 33)

STRIDE: Repudiation  
7. Repudiation of Exposure Notifications  -
  User claims never receiving or acknowledging exposure alerts; lack of non‑repudiation.  
  DREAD – D:4, R:6, E:5, A:7, D:6 (Total 28)

8. Repudiation of Data Uploads  -
  BackendServer or user denies having uploaded/downloaded contact logs.  
  DREAD – D:4, R:6, E:5, A:7, D:6 (Total 28)

STRIDE: Information Disclosure  
9. Unauthorized BLE Data Eavesdropping  +
  Third‑party devices sniff UUID exchanges over Bluetooth to track contacts.  
  DREAD – D:6, R:8, E:7, A:9, D:8 (Total 38)

10. Unauthorized GPS Data Disclosure  -
  Exfiltration of raw GPS logs from MobileApp before anonymization.  
  DREAD – D:7, R:7, E:7, A:8, D:7 (Total 36)

11. Backend Data Breach  +
  Compromise of UserDatabase exposes contact and location logs at rest.  
  DREAD – D:9, R:5, E:5, A:9, D:5 (Total 33)

12. Inference from Aggregated Data  +
  HealthAuthority’s shared aggregates allow re‑identification of individuals.  
  DREAD – D:6, R:6, E:6, A:7, D:6 (Total 31)

STRIDE: Denial of Service  
13. Backend Server DoS  +
  Flooding BackendServer with bogus uploads to disrupt service.  
  DREAD – D:5, R:7, E:6, A:9, D:7 (Total 34)

14. BLE Interface DoS  -
  Constant BLE scanning or malformed packets drain device resources.  
  DREAD – D:4, R:7, E:6, A:8, D:7 (Total 32)

15. Battery/Resource Exhaustion  +
  Malicious app triggers GPS and BLE continuously to drain user’s battery.  
  DREAD – D:4, R:7, E:7, A:8, D:8 (Total 34)

STRIDE: Elevation of Privilege  
16. Unauthorized Access to Device Sensors  +
  Malware elevates privileges on MobileApp to access BLEInterface or GPSInterface.  
  DREAD – D:6, R:5, E:5, A:8, D:5 (Total 29)

17. Privilege Escalation on Backend Server  -
  Attacker exploits a vulnerability to gain admin rights on BackendServer.  
  DREAD – D:9, R:4, E:4, A:9, D:4 (Total 30)