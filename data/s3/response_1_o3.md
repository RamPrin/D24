# Model:
```python
from pytm import TM, Boundary, Server, Actor, Dataflow

tm = TM("Amazon S3 Threat Model")

# Boundaries
internet = Boundary("Internet")
aws_cloud = Boundary("AWS Cloud")

# Components
user = Actor("User", boundary=internet)
s3_service = Server("S3 Service", boundary=aws_cloud)
s3_bucket = Server("S3 Bucket", boundary=aws_cloud)
iam = Server("IAM Service", boundary=aws_cloud)
kms = Server("KMS", boundary=aws_cloud)
cloudtrail = Server("CloudTrail", boundary=aws_cloud)

# Dataflows
Dataflow(user, s3_service, "S3 API Calls (Create/List/Upload/Retrieve/Delete/Presign)")
Dataflow(s3_service, iam, "Policy & ACL Evaluation")
Dataflow(s3_service, kms, "Server‑Side Encryption/Decryption")
Dataflow(s3_service, s3_bucket, "Store/Retrieve Object Data & Metadata")
Dataflow(s3_service, cloudtrail, "Log API Events")
Dataflow(s3_bucket, s3_bucket, "Cross‑Region Replication")

tm.process()
``` 

# Threats

Spoofing:
- User Credential Theft: Attacker obtains AWS access keys or session tokens to impersonate a legitimate user.
- Pre‑Signed URL Abuse: Unauthorized party reuses or forges pre‑signed URLs to access private objects.
- Role Assumption Spoofing: Malicious actor tricks AWS STS into issuing temporary credentials for a privileged role.
- API Endpoint Spoofing: Attacker directs user to a fake S3 endpoint to harvest credentials.

Tampering:
- In‑Transit Data Modification: Intercepted object data is altered during upload or download.
- Bucket Policy/ACL Tampering: Unauthorized modification of bucket policies or ACLs to change permissions.
- Object Metadata Tampering: Attacker modifies metadata (e.g., content-type) to evade detection or trigger misbehavior.
- Log Tampering: Deletion or modification of CloudTrail logs to cover tracks.
- Replication Stream Interference: Altering data during cross‑region replication to inject malicious content.

Repudiation:
- Action Denial: User denies having performed object deletion or modification; logs are insufficiently detailed.
- Incomplete Logging: CloudTrail or S3 access logging gaps prevent reliable audit of API calls.
- Versioning Dispute: Without versioning enabled, it’s impossible to prove prior existence or deletion of objects.
- Pre‑Signed URL Non‑Attribution: Access via pre‑signed URLs lacks user identity linkage, complicating accountability.

Information Disclosure:
- Public Bucket Misconfiguration: Bucket policy or ACL grants unintended public read or list permissions.
- ACL Over‑Granting: Object ACLs allow read/write by unauthorized AWS accounts or groups.
- Pre‑Signed URL Leakage: Shared or logged URLs expose private objects to unintended recipients.
- KMS Key Exposure: Weak or broadly shared KMS policies allow unauthorized decryption of objects.
- Logging Data Exposure: Sensitive request parameters recorded in CloudTrail become accessible to attackers with log access.

Denial of Service:
- API Request Flooding: Excessive List/Upload/Delete requests exceed S3 rate limits, causing service throttling.
- Storage Exhaustion: Attacker uploads large volumes of data to consume quota or drive up costs.
- KMS Throttling DoS: High volume of encryption/decryption requests exhaust KMS throughput limits.
- Replication Loop Flood: Misconfigured replication rules trigger continuous replication storms between buckets.
- Network Bandwidth Saturation: Large-scale data transfers to/from S3 degrade network availability for other services.

Elevation of Privilege:
- Over‑Permissive IAM Policies: Granting `s3:*` on `*` allows users to modify bucket policies and elevate privileges.
- Cross‑Account Trust Abuse: Exploiting overly broad external principal in bucket policy to gain unauthorized access.
- KMS Key Policy Misconfiguration: Granting users `kms:*` on a CMK allows decryption/encryption of any S3 object.
- Service Role Compromise: Hijacking the IAM role used by replication or logging to perform privileged actions.
- Metadata‑Driven Escalation: Using user‑defined metadata fields to inject policy changes or script execution on retrieval.