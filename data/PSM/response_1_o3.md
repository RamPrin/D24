# Model:
```python
from pytm import TM, Boundary, Actor, Process, Datastore, Dataflow

tm = TM("Password Storage Module", description="Threat model for a secure password storage component")

# Boundaries
external = Boundary("External Network")
internal = Boundary("Internal Network")

# Components
user = Actor("User", boundary=external)
auth_service = Process("AuthService", boundary=internal)
psm = Process("PasswordStorageModule", boundary=internal)
password_db = Datastore("PasswordDatabase", boundary=internal)
audit_log = Datastore("AuditLog", boundary=internal)

# Dataflows
Dataflow(user, auth_service, "Submit password", protocol="HTTPS", tls="TLS")
Dataflow(auth_service, psm, "Hash/Verify password", encryption="AES")
Dataflow(psm, password_db, "Store/Retrieve hash+salt", encryption="AES")
Dataflow(psm, audit_log, "Write audit entry", encryption="AES")

tm.process()
```

# Threats

Spoofing:
- User Impersonation: Attacker masquerades as a legitimate user to submit credentials and gain unauthorized access.
- Service Spoofing: Attacker poses as AuthService to trick the PSM into processing malicious requests.
- Component Impersonation: Malicious process pretends to be the PSM to intercept or manipulate password flows.

Tampering:
- In‑Transit Modification: Attacker intercepts and alters password or hash traffic between AuthService and PSM.
- Database Tampering: Attacker modifies stored hashes or salts in PasswordDatabase to bypass authentication.
- Audit Log Manipulation: Unauthorized party alters or deletes entries in AuditLog to cover tracks.
- Configuration Tampering: Attacker changes PSM configuration (e.g., KDF iteration count) to weaken security.

Repudiation:
- Log Deletion: Actor deletes or modifies audit logs to deny having performed sensitive operations.
- Incomplete Logging: Missing or insufficient audit entries let a user repudiate registration or login events.
- Timestamp Manipulation: Modification of log timestamps to dispute the timing of authentication or changes.

Information Disclosure:
- Cleartext Exposure: Passwords are logged or cached in cleartext in AuthService or PSM logs.
- Hash/​Salt Leakage: Database compromise leads to exposure of password hashes and salts for offline cracking.
- Side‑Channel Leakage: Timing or error messages during verification reveal information about password validity.
- Backup Exposure: Insecure backups of PasswordDatabase or keys lead to bulk disclosure of credentials.

Denial of Service:
- KDF Exhaustion: Attacker floods PSM with hash/verify requests to exhaust CPU resources.
- Storage Exhaustion: Attacker injects large or frequent entries to fill up PasswordDatabase or AuditLog.
- Network Flooding: DDoS on AuthService or PSM disrupts legitimate authentication traffic.
- Backup Lockout: Corruption or unavailability of backups prevents recovery after legitimate failures.

Elevation of Privilege:
- API Abuse: Unauthorized user exploits weak PSM API endpoints to read or write password data directly.
- Privilege Escalation in PSM: Flawed access control in PSM allows low‑privilege processes to perform high‑privilege operations.
- Injection Attacks: SQL or command injection on PasswordDatabase allows execution of arbitrary queries or code.
- Misconfigured Encryption Keys: Attacker with partial access uses weak key management to decrypt entire database.