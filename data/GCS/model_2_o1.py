
from pytm import TM, Actor, Process, Dataflow, Asset, Server

# Define threat model
tm = TM("Google Cloud Storage Threat Model")

# Define actors
user = Actor("User")

# Define components
bucket = Asset("Bucket")
object_storage = Asset("Object Storage")
kms = Server("Google Cloud Key Management Service (KMS)")
acl = Asset("Access Control List")
iam = Asset("IAM Policies")

# Define processes
create_bucket = Process("Create Bucket")
upload_object = Process("Upload Object")
retrieve_object = Process("Retrieve Object")
delete_object = Process("Delete Object")
list_objects = Process("List Objects")

# Define dataflows
Dataflow(user, create_bucket, "Request to create bucket")
Dataflow(user, upload_object, "Upload object to bucket")
Dataflow(user, retrieve_object, "Retrieve object from bucket")
Dataflow(user, delete_object, "Delete object from bucket")
Dataflow(user, list_objects, "List objects in bucket")

# Define dataflows to assets
Dataflow(upload_object, bucket, "Store object")
Dataflow(bucket, retrieve_object, "Access object")
Dataflow(delete_object, bucket, "Remove object")
Dataflow(list_objects, bucket, "Query objects")

# Access control and security dataflows
Dataflow(bucket, acl, "Apply ACL settings")
Dataflow(bucket, iam, "Apply IAM policies")
Dataflow(object_storage, kms, "Encrypt object")

# Set trust boundaries
bucket.inBoundary = True
object_storage.inBoundary = True

# Define storage location
bucketHashed = bucket.hashed  # Simulate bucket being region or multi-regional
objectStored = object_storage.hashed  # Simulate object storage location

# Define authentication and authorization controls
acl.check_authentication = True
iam.check_authentication = True

tm.process()