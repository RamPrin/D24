
from pytm import TM, Actor, Boundary, Data, Process, Store

# Define the threat model
tm = TM("Amazon S3 Threat Model")

# External entities
users = Actor("Users")
aws_services = Actor("AWS Services")

# Define boundaries
internet = Boundary("Internet")

# Define data stores
bucket = Store("Bucket")
object_store = Store("Object Store")

# Define processes
create_bucket = Process("Create Bucket")
upload_object = Process("Upload Object")
retrieve_object = Process("Retrieve Object")
delete_object = Process("Delete Object")
list_objects = Process("List Objects")

# Define data assets
bucket_data = Data("Bucket Data")
object_data = Data("Object Data")
access_control_data = Data("Access Control Data")
encryption_data = Data("Encryption Data")

# Define data flows
users >> internet >> create_bucket >> bucket
users >> internet >> upload_object >> object_store
aws_services >> internet >> retrieve_object >> object_store
users >> internet >> delete_object >> object_store
users >> internet >> list_objects >> object_store

# Access control flows
access_control_data >> bucket
access_control_data >> object_store

# Encryption flows
encryption_data >> object_store

# Add elements to the threat model
tm += [
    users,
    aws_services,
    internet,
    bucket,
    object_store,
    create_bucket,
    upload_object,
    retrieve_object,
    delete_object,
    list_objects,
    bucket_data,
    object_data,
    access_control_data,
    encryption_data,
]

# Define threats
tm.process()

# Print a summary
tm.report()