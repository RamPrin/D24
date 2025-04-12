from pytm import TM, Actor, Boundary, Dataflow, Server, Process

# Define Threat Model
tm = TM("IoT Authentication Threat Model")

# Define Boundaries
iot_network = Boundary("IoT Network")
internet = Boundary("Internet")

# Define Actors
end_user = Actor("End User")
administrator = Actor("Administrator")

# Define Servers and Systems
iot_device = Server("IoT Device")
gateway = Server("Gateway")
cloud_service = Server("Cloud Services")
auth_server = Server("Authentication Server")
directory_service = Server("Directory Services")
hsm = Server("Hardware Security Module")

# Define Dataflows
df1 = Dataflow(end_user, iot_device, "User Authentication")
df2 = Dataflow(iot_device, gateway, "Device Authentication")
df3 = Dataflow(gateway, cloud_service, "Device Data")
df4 = Dataflow(cloud_service, auth_server, "Authentication Request")
df5 = Dataflow(auth_server, directory_service, "Credential Verification")
df6 = Dataflow(auth_server, hsm, "Key Management")

# Assign Boundaries
iot_device.inBoundary = iot_network
gateway.inBoundary = iot_network
cloud_service.inBoundary = internet
auth_server.inBoundary = internet
directory_service.inBoundary = internet
hsm.inBoundary = internet

# Process Threat Model
tm.process()