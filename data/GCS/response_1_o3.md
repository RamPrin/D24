# Model:
```python
from pytm import TM, Boundary, Person, Process, DataStore, DataFlow

tm = TM("Google Cloud Storage Threat Model")

# Boundaries
internet = Boundary("Internet")
gcp = Boundary("GCP Infrastructure")

# Components
user = Person("External User")
console = Process("Cloud Console")
sdk = Process("Client SDK")
api = Process("GCS REST API")
iam = Process("IAM Service")
kms = Process("KMS Service")
lifecycle = Process("Lifecycle Management")
replication = Process("Replication Service")
buckets = DataStore("Buckets")
objects = DataStore("Objects")
audit_logs = DataStore("Audit Logs")

# Assign components to boundaries
internet.add_entity(user)
internet.add_entity(console)
internet.add_entity(sdk)

gcp.add_entity(api)
gcp.add_entity(iam)
gcp.add_entity(kms)
gcp.add_entity(lifecycle)
gcp.add_entity(replication)
gcp.add_entity(buckets)
gcp.add_entity(objects)
gcp.add_entity(audit_logs)

# Data Flows
DataFlow(user, console, "Access via Web Console", "HTTPS")
DataFlow(user, sdk, "Access via SDK/CLI", "HTTPS")
DataFlow(console, api, "REST API Calls", "HTTPS")
DataFlow(sdk, api, "REST API Calls", "HTTPS")
DataFlow(api, iam, "Authenticate/Authorize Request", "HTTPS")
DataFlow(api, kms, "Key Encryption/Decryption", "TLS")
DataFlow(api, buckets, "Manage Buckets", "HTTPS")
DataFlow(api, objects, "Upload/Download Objects", "HTTPS")
DataFlow(api, audit_logs, "Log API Calls", "Internal Secure Channel")
DataFlow(buckets, replication, "Cross-Region Replication", "Internal Secure Channel")
DataFlow(lifecycle, buckets, "Apply Lifecycle Rules", "Internal Secure Channel")

tm.process()
``` 
# Threats
Spoofing:
- Credential Theft: Attacker steals user or service account credentials to impersonate legitimate users.
- Signed URL Forgery: Attacker crafts or replays signed URLs to gain unauthorized object access.
- API Endpoint Spoofing: DNS or MITM attack redirects SDK/Console calls to a malicious endpoint.
- KMS Service Impersonation: Attacker mimics KMS to supply attacker-controlled keys.

Tampering:
- In-Transit Data Tampering: Alter object data or metadata during upload/download if TLS is broken.
- Bucket Policy Tampering: Unauthorized modification of bucket IAM policies or ACLs.
- Object Metadata Modification: Malicious change of object metadata (e.g., content-type, retention).
- Audit Log Tampering: Deletion or modification of audit logs to cover malicious actions.

Repudiation:
- Log Deletion: Insider deletes or disables Cloud Audit Logs to hide actions.
- Insufficient Logging: Missing detailed logs (e.g., source IP, timestamp) allows denial of actions.
- Unsynchronized Clocks: Clock skew across services prevents reliable event ordering and non-repudiation.
- Unlinked Actions: Actions performed by chained service accounts lack binding to original user.

Information Disclosure:
- Public Bucket Exposure: Misconfigured ACLs or policies make buckets or objects publicly readable.
- Unencrypted Data in Transit: Downgrade attacks force non‑TLS channels exposing data.
- KMS Key Exposure: Compromise of encryption keys in KMS leaks object contents at rest.
- Cross-Region Leak: Replication service misconfiguration exposes data across projects or regions.
- Metadata Leakage: Sensitive metadata (e.g., object names, sizes) exposed via list operations.

Denial of Service:
- API Rate Limit Exhaustion: Flooding REST API to exhaust project’s quota, blocking legitimate calls.
- Storage Quota Exhaustion: Attacker uploads large volumes of data to consume customer’s storage quota.
- Large Object Upload Attacks: Repeated huge multipart uploads destabilize service performance.
- Replication Storm: Abuse of cross‑region replication to saturate internal network.
- Lifecycle Policy Misuse: Crafting rapid versioning/lifecycle rules to trigger massive deletions or transitions.

Elevation of Privilege:
- Overly Permissive IAM Roles: Granting broad roles (e.g., Storage Admin) allows privilege escalation.
- ACL Misconfiguration: Public “allUsers” write permissions enable unauthorized data writes.
- Cross-Project Access: Service account misbinding across projects grants unintended access.
- KMS IAM Policy Misconfiguration: Weak KMS key policies allow non‑owners to decrypt or re‑encrypt data.
- Service Account Impersonation: Exploiting GCP IAM to impersonate higher‑privilege service accounts.
