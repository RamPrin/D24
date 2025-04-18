
from pytm import TM, Boundary, ExternalEntity, Server, Datastore, Process, Dataflow, Encryption

tm = TM("Google Cloud Storage Threat Model")

internet = Boundary("Internet")
gcp = Boundary("GCP Cloud")

user = ExternalEntity("GCS User", description="Authenticated principal via IAM", boundary=internet)
attacker = ExternalEntity("Attacker", description="Unauthenticated or malicious actor", boundary=internet)

gcs_api = Server("GCS API", description="REST API endpoint for bucket/object operations", boundary=gcp)
kms = Server("Cloud KMS", description="Key management service for encryption keys", boundary=gcp)
bucket = Datastore("GCS Bucket", description="Container for objects (versioning, lifecycle rules)", boundary=gcp)

# API operations
Dataflow(user, gcs_api, "HTTPS API Request (Create/Upload/Retrieve/Delete/List)", protocols="HTTPS", data="Request Params, Object Data")
Dataflow(attacker, gcs_api, "HTTPS Malicious API Request", protocols="HTTPS", data="Malformed or unauthorized payload")
Dataflow(gcs_api, user, "HTTPS API Response", protocols="HTTPS", data="Status, Object Data or Error")

# Internal storage flows
Dataflow(gcs_api, bucket, "Store/Retrieve Object Data & Metadata", protocols="gRPC", data="Object Data, Metadata")
Dataflow(bucket, gcs_api, "Object Data & Metadata", protocols="gRPC")

# KMS integration
Dataflow(gcs_api, kms, "Request DEK (Data Encryption Key)", protocols="gRPC", data="KeyID")
Dataflow(kms, gcs_api, "Return DEK", protocols="gRPC", data="Encrypted DEK")

# Encryption at rest
Encryption(gcs_api, bucket, "Server‑side encryption with CMEK (AES256)")