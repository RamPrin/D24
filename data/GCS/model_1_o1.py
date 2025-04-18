from pytm import TM, Boundary, Server, Dataflow, Datastore, Actor

# Define the threat model
tm = TM("Google Cloud Storage Threat Model")

# Define boundaries
internet_boundary = Boundary("Internet")
gcp_boundary = Boundary("Google Cloud Platform")

# Define components
user = Actor("User", inBoundary=internet_boundary)
bucket = Datastore("Bucket", inBoundary=gcp_boundary)
object_storage = Server("Object Storage Service", inBoundary=gcp_boundary)

# Define dataflows
df1 = Dataflow(user, bucket, "Create Bucket")
df2 = Dataflow(user, object_storage, "Upload Object")
df3 = Dataflow(object_storage, user, "Retrieve Object")
df4 = Dataflow(user, object_storage, "Delete Object")
df5 = Dataflow(user, object_storage, "List Objects")

# Process the threat model
tm.process()