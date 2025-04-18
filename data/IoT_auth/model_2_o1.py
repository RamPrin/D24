
from pytm import TM, Actor, Asset, Dataflow, Server, Process, Boundary

tm = TM("IoT Authentication Threat Model")

# Core Components
iot_device = Asset("IoT Device")
embedded_system = Asset("Embedded System")
end_user = Actor("End User")
admin = Actor("Administrator")
gateway = Asset("Gateway")
cloud_service = Server("Cloud Services")
auth_server = Server("Authentication Server")

# Authentication Mechanisms
psk = Dataflow(iot_device, auth_server, "Pre-Shared Keys")
pki = Dataflow(iot_device, auth_server, "Public Key Infrastructure")
certificate = Dataflow(iot_device, auth_server, "Certificates")
hsm = Asset("Hardware Security Module")
biometric_auth_device = Dataflow(iot_device, auth_server, "Biometric Authentication")

username_password = Dataflow(end_user, gateway, "Username and Password")
mfa = Dataflow(end_user, gateway, "Multi-Factor Authentication")
biometric_auth_user = Dataflow(end_user, gateway, "Biometric Authentication")
sso = Dataflow(end_user, gateway, "Single Sign-On")

api_key = Dataflow(cloud_service, gateway, "API Keys")
oauth = Dataflow(cloud_service, gateway, "OAuth/OAuth 2.0")
jwt = Dataflow(cloud_service, gateway, "JWT (JSON Web Tokens)")

# Authentication Protocols
tls_ssl = Dataflow(gateway, cloud_service, "TLS/SSL")
mqtt_tls = Dataflow(gateway, iot_device, "MQTT with TLS")
coap_dtls = Dataflow(iot_device, gateway, "CoAP with DTLS")
custom_protocol = Dataflow(iot_device, auth_server, "Custom Protocols")

# Key Considerations
key_management = Process("Key Management")
monitoring_logging = Process("Monitoring and Logging")

# Boundaries
internet_boundary = Boundary("Internet")
iot_network_boundary = Boundary("IoT Network")

# Linking elements
iot_device.inBoundary = iot_network_boundary
gateway.inBoundary = iot_network_boundary
cloud_service.inBoundary = internet_boundary
auth_server.inBoundary = internet_boundary

tm.threatsFile = "threats.json"
tm.process() 