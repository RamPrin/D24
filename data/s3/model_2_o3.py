
from pytm import TM, Actor, Process, Datastore, Boundary, Dataflow, Encryption

tm = TM("Amazon S3 Threat Model")

# Boundaries
internet = Boundary("Internet")
aws = Boundary("AWS Cloud")

# Actors
user = Actor("User", boundary=internet)
attacker = Actor("Attacker", boundary=internet)

# Components
s3_bucket = Datastore(
    "S3 Bucket",
    boundary=aws,
    technology="Amazon S3",
    description="Container for objects and metadata"
)
kms = Datastore(
    "KMS",
    boundary=aws,
    technology="AWS KMS",
    description="Key management for encryption"
)
pre_signed_service = Process(
    "Pre‑signed URL Service",
    boundary=aws,
    technology="AWS SDK",
    description="Generates temporary object access URLs"
)
versioning_lifecycle = Process(
    "Versioning & Lifecycle Manager",
    boundary=aws,
    description="Handles object versioning and lifecycle policies"
)
replicator = Process(
    "Cross‑Region Replicator",
    boundary=aws,
    description="Replicates objects across regions"
)

# Data flows
Dataflow(user, s3_bucket, "Upload Object", protocol="HTTPS")
Dataflow(user, s3_bucket, "Download Object", protocol="HTTPS")
Dataflow(user, s3_bucket, "List Objects", protocol="HTTPS")
Dataflow(pre_signed_service, user, "Presigned URL", protocol="HTTPS")
Dataflow(s3_bucket, s3_bucket, "Replication", technology="S3 Replication", note="Cross‑region")
Encryption(s3_bucket, kms, description="Server‑side encryption using KMS")

# Threats
s3_bucket.threats = [
    "Unauthorized access via misconfigured ACL/Bucket Policy",
    "Data exfiltration from compromised credentials",
    "DoS via request flooding",
    "MITM on endpoints if TLS downgraded",
    "Accidental public exposure"
]
pre_signed_service.threats = [
    "URL replay before expiry",
    "Leak of pre‑signed URLs"
]
kms.threats = [
    "Compromise of KMS keys",
    "Insider misuse of key material"
]
versioning_lifecycle.threats = [
    "Unauthorized deletion bypass via versioning",
    "Lifecycle misconfig leading to data loss"
]
replicator.threats = [
    "Replication to unauthorized regions",
    "Eavesdropping on replication channel"
]

tm.process()