Spoofing  
1. User Identity Spoofing  
   Attacker impersonates a legitimate user to submit passwords to the PSM.  
   DREAD – D=7, R=8, E=7, A=8, Di=6 (Sum=36)  

2. Component Impersonation  
   Attacker spoofs the backup storage endpoint to intercept or alter encrypted snapshots.  
   DREAD – D=5, R=6, E=6, A=7, Di=6 (Sum=30)  

Tampering  
3. Data Tampering in Transit  
   Attacker intercepts and modifies the password submitted over TLS before hashing.  
   DREAD – D=6, R=9, E=8, A=7, Di=8 (Sum=38)  

4. Tampering with Stored Hashes  
   Attacker exploits a DB vulnerability to modify or inject forged encrypted hash+salt entries.  
   DREAD – D=7, R=8, E=7, A=8, Di=7 (Sum=37)  

5. Tampering with Backup  
   Attacker corrupts or alters the encrypted backup snapshot, preventing valid restores.  
   DREAD – D=5, R=7, E=6, A=7, Di=6 (Sum=31)  

Repudiation  
6. User Action Repudiation  
   Lack of secure audit logging allows a user to deny having submitted or changed a password.  
   DREAD – D=4, R=6, E=5, A=5, Di=4 (Sum=24)  

7. Admin Action Repudiation  
   Administrators can deny initiating or approving critical operations (e.g., DB deletion).  
   DREAD – D=4, R=5, E=4, A=5, Di=4 (Sum=22)  

Information Disclosure  
8. Password Disclosure over Network  
   Weak or misconfigured TLS allows eavesdropping of plaintext passwords in flight.  
   DREAD – D=7, R=8, E=8, A=9, Di=7 (Sum=39)  

9. Disclosure of Intermediate Values  
   Attacker intercepts derived key and hash between the Hash & KDF and Encrypt Storage processes.  
   DREAD – D=6, R=7, E=7, A=8, Di=7 (Sum=35)  

10. Database Breach  
    Attacker reads the encrypted password database, enabling offline cracking attempts.  
    DREAD – D=8, R=8, E=7, A=9, Di=8 (Sum=40)  

11. Backup Storage Breach  
    Attacker compromises backup storage and exfiltrates encrypted snapshots for offline analysis.  
    DREAD – D=7, R=7, E=7, A=9, Di=8 (Sum=38)  

Denial of Service  
12. Hashing Resource Exhaustion  
    Attacker floods the Hash & KDF process, exhausting CPU and delaying legitimate requests.  
    DREAD – D=6, R=9, E=8, A=8, Di=7 (Sum=38)  

13. Database Unavailability  
    Attacker deletes or locks the Password Database, preventing authentication.  
    DREAD – D=7, R=8, E=8, A=9, Di=7 (Sum=39)  

14. Backup Storage Flood  
    Attacker writes excessive data to backup storage, exhausting disk space and blocking backups.  
    DREAD – D=5, R=7, E=7, A=8, Di=6 (Sum=33)  

Elevation of Privilege  
15. Code Injection in Hash & KDF Module  
    Vulnerability allows attacker to inject and execute arbitrary code in the hashing component.  
    DREAD – D=8, R=6, E=6, A=8, Di=7 (Sum=35)  

16. Encryption Module Buffer Overflow  
    Attacker exploits a buffer‑overflow in the encryption process to escalate privileges.  
    DREAD – D=8, R=6, E=6, A=8, Di=7 (Sum=35)  

17. KDF Parameter Tampering  
    Attacker with limited access alters KDF parameters (e.g., low iteration count) to weaken password protection.  
    DREAD – D=7, R=7, E=7, A=8, Di=7 (Sum=36)