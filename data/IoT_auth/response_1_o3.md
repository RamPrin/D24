# Model:
```python
from pytm import TM, Boundary, Actor, Server, Dataflow, DataStore

tm = TM("IoT Authentication")

# Trust boundaries
bd_iot = Boundary("IoT_Zone")
bd_cloud = Boundary("Cloud_Zone")
bd_auth = Boundary("Auth_Zone")

# Components
device = Actor("IoT_Device", boundary=bd_iot)
gateway = Server("Gateway", boundary=bd_iot)
cloud = Server("Cloud_Service", boundary=bd_cloud)
end_user = Actor("End_User", boundary=bd_cloud)
admin = Actor("Administrator", boundary=bd_cloud)
auth_server = Server("Auth_Server", boundary=bd_auth)
hsm = Server("HSM", boundary=bd_auth)
directory = DataStore("Directory_Service", boundary=bd_auth)

# Dataflows
Dataflow(device, gateway, "MQTT over TLS")
Dataflow(gateway, cloud, "HTTPS")
Dataflow(end_user, cloud, "Web/API requests over TLS")
Dataflow(admin, auth_server, "Admin console over TLS")
Dataflow(cloud, auth_server, "Auth requests over TLS")
Dataflow(auth_server, directory, "Credential lookup")
Dataflow(auth_server, hsm, "Key operations")

tm.process()
``` 


# Threats
Spoofing:
- Device Impersonation: Attacker forges device credentials to masquerade as a legitimate IoT device.
- Gateway Spoofing: Malicious actor poses as the gateway to intercept or reroute device communications.
- User Credential Theft: Attacker steals or guesses user credentials to access cloud services as a valid user.
- Admin Account Takeover: Compromised administrator credentials allow full control of authentication infrastructure.
- Auth Server Masquerade: Attacker pretends to be the authentication server to capture credentials or tokens.

Tampering:
- Message Tampering in Transit: Attacker alters MQTT or HTTPS payloads to inject malicious commands or corrupt data.
- Firmware Tampering: Unauthorized modification of device firmware to subvert authentication checks.
- Log Tampering: Modification or deletion of authentication logs in Cloud_Service or Auth_Server to cover tracks.
- Configuration Tampering: Unauthorized changes to gateway or cloud configuration to disable security controls.
- Directory Data Tampering: Manipulation of stored credentials in Directory_Service to grant unauthorized access.

Repudiation:
- Insufficient Logging: Lack of detailed logs prevents proving which device or user initiated an action.
- Log Erasure by Insider: Administrator erases or modifies logs on Auth_Server to deny responsibility for a breach.
- Transaction Denial: User or device denies having sent critical commands or data, and no non-repudiation mechanism exists.
- Audit Trail Gaps: Missing or inconsistent records between Cloud_Service and Auth_Server leave actions untraceable.

Information Disclosure:
- Eavesdropping on MQTT: Attacker intercepts unencrypted or poorly encrypted MQTT traffic to read device data.
- Credentials in Logs: Sensitive tokens or keys written to logs in Cloud_Service or Gateway expose secrets.
- Misconfigured API: Overly verbose error messages in Cloud_Service reveal internal implementation details.
- HSM Side‑Channel Leak: Physical or timing side-channel from HSM exposes private keys.
- Directory Service Data Leak: Unauthorized read access to Directory_Service reveals user and device credentials.

Denial of Service:
- MQTT Flooding: Attacker floods the gateway with MQTT connection requests causing resource exhaustion.
- TLS Handshake Exhaustion: Rapidly opening and closing TLS sessions to overload Cloud_Service or Auth_Server.
- HSM Resource Starvation: Excessive key operation requests deny legitimate cryptographic operations.
- Gateway Device Overload: DoS at the IoT_Zone gateway blocks all device–cloud communication.
- Authentication Server Crash: Malformed authentication requests exploit a bug, crashing Auth_Server.

Elevation of Privilege:
- Device-to-Gateway Exploit: Compromised IoT_Device exploits a vulnerability in Gateway to gain higher privileges.
- Role Escalation via API: End_User exploits misconfigured Cloud_Service API to perform administrator actions.
- Token Forgery: Attacker crafts or replays JWT/OAuth tokens to gain unauthorized access to services.
- Administrator Interface Flaw: Exploitation of admin console on Auth_Server grants system‑level control.
- Cross‑Component Exploit: Compromise of Gateway used as pivot to attack Auth_Server and HSM with elevated rights.
