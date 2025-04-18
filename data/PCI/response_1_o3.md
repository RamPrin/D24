# Model:
```python
from pytm import TM, Boundary, Actor, Server, DataFlow, DataStore

tm = TM("PCI DSS Compliance Environment")

# Boundaries
b_external = Boundary("External Network")
b_cde      = Boundary("Cardholder Data Environment")
b_internal = Boundary("Internal Corporate Network")
b_qsa      = Boundary("QSA Boundary")

# Actors
cardholder = Actor("Cardholder", boundary=b_external)
merchant   = Actor("Merchant Staff", boundary=b_internal)
qsa        = Actor("Qualified Security Assessor", boundary=b_qsa)
bank       = Actor("Acquiring Bank", boundary=b_external)

# Components
web_server   = Server("Web Server", boundary=b_external)
app_server   = Server("Application Server", boundary=b_cde)
db_server    = Server("Database Server", boundary=b_cde)
log_store    = DataStore("Log Store", boundary=b_internal)
siem         = Server("SIEM", boundary=b_internal)
assessment   = Server("Self‐Assessment System", boundary=b_internal)
roc_store    = DataStore("RoC Repository", boundary=b_qsa)

# Dataflows
DataFlow(cardholder, web_server,   "Submit Payment Details",       protocols="HTTPS")
DataFlow(web_server, app_server,   "Forward Payment Request",      protocols="Internal API")
DataFlow(app_server, db_server,    "Query/Store Cardholder Data",  protocols="Encrypted DB")
DataFlow(app_server, log_store,    "Write Transaction Logs",        protocols="TLS")
DataFlow(log_store, siem,          "Log Forwarding",               protocols="Syslog/TLS")
DataFlow(merchant, assessment,     "Upload Self‐Assessment Data",  protocols="HTTPS")
DataFlow(assessment, qsa,          "Send Assessment Reports",      protocols="SFTP")
DataFlow(qsa, roc_store,           "Store Validated RoC",          protocols="SFTP")
DataFlow(roc_store, bank,          "Submit RoC to Bank",           protocols="SFTP")

tm.process()
```

# Threats

Spoofing:
- Unauthorized Cardholder Impersonation: Attacker uses stolen PAN and CVV to masquerade as a legitimate cardholder.
- Default Credential Exploitation: Attacker leverages vendor‑supplied default passwords on servers to gain access.
- IP Spoofing to Bypass Firewall: Attacker spoofs internal IP addresses to pass firewall rules.
- QSA Identity Forgery: Unauthorized party impersonates a Qualified Security Assessor to submit fake RoC.
- Merchant Staff Account Spoofing: Attacker guesses or reuses credentials to appear as authorized staff.

Tampering:
- In‑Transit Data Modification: Attacker intercepts and alters PAN or transaction details on the wire.
- Log File Tampering: Malicious insider or attacker modifies or deletes log entries to cover tracks.
- Configuration File Alteration: Attacker changes encryption or firewall configs to weaken protections.
- Database Record Tampering: Unauthorized change of stored cardholder data to commit fraud.
- AV Definition Tampering: Attacker corrupts antivirus signature database to disable malware detection.

Repudiation:
- Transaction Denial by Cardholder: Cardholder refuses to acknowledge a legitimate transaction.
- Assessment Report Dispute: Merchant claims QSA report was never delivered or was altered.
- Log Integrity Dispute: Insider denies actions, alleging logs are incomplete or tampered.
- RoC Submission Denial: Acquiring bank disputes receipt of the RoC, claiming non‑delivery.

Information Disclosure:
- Eavesdropping on PAN: Attacker captures unencrypted PAN on public or internal networks.
- Stored Data Exposure: Unauthorized retrieval of database backups containing cardholder data.
- Misconfigured Storage Bucket: Publicly accessible backup or RoC repository leaks sensitive data.
- Log Data Leakage: Sensitive card details in logs exposed to unauthorized viewers.
- Assessment Data Interception: Self‑assessment data in transit to QSA captured in clear.

Denial of Service:
- Firewall Flooding: High volume traffic overwhelms firewall, blocking legitimate transactions.
- Web Server Application DoS: Attackers exploit application logic to exhaust server resources.
- Database Connection Starvation: Excessive bogus requests exhaust DB connection pool.
- SIEM Overload: Log storm causes SIEM to drop alerts or become unresponsive.
- Assessment System DoS: Targeted attack prevents self‑assessment uploads, delaying compliance.

Elevation of Privilege:
- Local Privilege Escalation on App Server: Exploit unpatched vulnerability to gain root/admin.
- Misconfigured ACLs on DB: Unauthorized user gains write access to CDE database.
- SIEM Admin Takeover: Weak credentials allow attacker to assume SIEM administrator role.
- Assessment System Privilege Escalation: Attacker escalates from merchant user to QSA role.
- Container Escape on Web Server: Attacker breaks out of container to gain host‑level access.