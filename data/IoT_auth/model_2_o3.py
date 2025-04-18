
from pytm import TM, Actor, Server, Process, DataStore, Boundary, Dataflow

tm = TM("IoT Authentication Threat Model")

# Boundaries
internet = Boundary("Internet")
dmz = Boundary("DMZ")
internal = Boundary("Internal Network")

# Actors
iot_device = Actor("IoT Device")
iot_device.boundary = internet

end_user = Actor("End User")
end_user.boundary = internet

admin = Actor("Administrator")
admin.boundary = internal

# Processes / Servers / DataStores
gateway = Process("IoT Gateway")
gateway.boundary = dmz

auth_server = Server("Authentication Server")
auth_server.boundary = internal

cloud_service = Server("Cloud Service")
cloud_service.boundary = internal

credential_store = DataStore("Credential Store")
credential_store.boundary = internal

# Data Flows
Dataflow(iot_device, gateway, "Device Registration\n(MQTT/TLS, PSK/Cert)")
Dataflow(gateway, auth_server, "Auth Request\n(OAuth2/TLS)")
Dataflow(auth_server, credential_store, "Verify Credentials\n(SQL over TLS)")
Dataflow(auth_server, gateway, "Auth Response\n(Token/JWT)")
Dataflow(end_user, cloud_service, "User Login\n(HTTPS, MFA)")
Dataflow(cloud_service, auth_server, "Token Validation\n(HTTPS)")
Dataflow(admin, auth_server, "Admin Access\n(SSH/TLS)")
Dataflow(cloud_service, credential_store, "Session Store Access\n(Encrypted)")

# To generate the report:
# tm.process()