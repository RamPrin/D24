
from pytm import TM, Boundary, Server, Dataflow, Actor, Datastore

# Define boundaries
internet = Boundary("Internet")
user_device = Boundary("User Device")
cloud = Boundary("Cloud Infrastructure")
health_authority = Boundary("Health Authority")

# Define actors
user = Actor("User")
public_health_official = Actor("Public Health Official")

# Define components
app_store = Server("App Store")
user_app = Server("Contact Tracing App", boundary=user_device)
server = Server("Application Server", boundary=cloud)
health_system = Server("Health System", boundary=health_authority)

# Define datastores
device_storage = Datastore("Device Storage", boundary=user_device)
cloud_storage = Datastore("Cloud Storage", boundary=cloud)
health_storage = Datastore("Health Authority Data", boundary=health_authority)

# Define dataflows
df1 = Dataflow(user, user_app, "Download App")
df2 = Dataflow(user_app, app_store, "App Updates")
df3 = Dataflow(user, user_app, "User Registration")
df4 = Dataflow(user_app, device_storage, "Store User Data")
df5 = Dataflow(user_app, server, "Bluetooth Proximity & Location Data")
df6 = Dataflow(server, cloud_storage, "Store Encrypted Data")
df7 = Dataflow(user_app, user, "Notifications")
df8 = Dataflow(server, health_system, "Share Anonymized Data")
df9 = Dataflow(health_system, public_health_official, "Data Insights")
df10 = Dataflow(user_app, server, "Submit Positive Test Result")
df11 = Dataflow(server, health_system, "Verify Test Result")
df12 = Dataflow(server, cloud_storage, "Data Retention and Deletion")

tm = TM("Contact Tracing Application")
tm.description = "A threat model for a contact tracing application used during infectious disease outbreaks."
tm.add_boundaries(internet, user_device, cloud, health_authority)
tm.add_actors(user, public_health_official)
tm.add_servers(app_store, user_app, server, health_system)
tm.add_datastores(device_storage, cloud_storage, health_storage)
tm.add_dataflows(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12)

tm.process()