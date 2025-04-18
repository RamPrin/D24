# Model:
```python
from pytm import TM, Boundary, Component, Dataflow

# Create threat model
tm = TM("IoT Supply Chain")

# Boundaries
iot_boundary = Boundary("IoT Devices")
network_boundary = Boundary("Network")
edge_boundary = Boundary("Edge Computing")
cloud_boundary = Boundary("Cloud Platform")
scm_boundary = Boundary("Supply Chain Systems")

# Components in IoT boundary
sensor = Component("Sensor", "Collects temperature/humidity/location", boundary=iot_boundary)
actuator = Component("Actuator", "Performs physical actions", boundary=iot_boundary)
rfid = Component("RFID Tag", "Identifies and tracks items", boundary=iot_boundary)
gps = Component("GPS Tracker", "Provides real-time location", boundary=iot_boundary)

# Components in Network boundary
wifi = Component("Wi-Fi Network", "Wireless connectivity", boundary=network_boundary)
bluetooth = Component("Bluetooth/Zigbee/LoRaWAN", "Local connectivity", boundary=network_boundary)
satellite = Component("Satellite Network", "Remote-area connectivity", boundary=network_boundary)

# Components in Edge boundary
edge = Component("Edge Processor", "Pre-processes IoT data", boundary=edge_boundary)

# Components in Cloud boundary
storage = Component("Cloud Storage", "Stores IoT data", boundary=cloud_boundary)
analytics = Component("Cloud Analytics", "Performs big data & ML", boundary=cloud_boundary)
api = Component("IoT API Gateway", "Exposes data to SCM", boundary=cloud_boundary)

# Components in SCM boundary
scm = Component("SCM System", "Manages end-to-end supply chain", boundary=scm_boundary)
ims = Component("Inventory Mgmt", "Tracks stock levels", boundary=scm_boundary)
tms = Component("Transport Mgmt", "Manages logistics", boundary=scm_boundary)
wms = Component("Warehouse Mgmt", "Handles warehouse ops", boundary=scm_boundary)

# Dataflows
Dataflow(sensor, wifi, "Telemetry", prot="TLS")
Dataflow(sensor, bluetooth, "Local telemetry", prot="AES")
Dataflow(rfid, wifi, "ID data", prot="None")
Dataflow(gps, satellite, "Location stream", prot="IPsec")
Dataflow(wifi, edge, "Aggregated telemetry", prot="TLS")
Dataflow(bluetooth, edge, "Local data", prot="AES")
Dataflow(satellite, edge, "Remote data", prot="IPsec")
Dataflow(edge, storage, "Upload batch data", prot="TLS")
Dataflow(edge, analytics, "Real-time feed", prot="TLS")
Dataflow(storage, api, "Data retrieval", prot="OAuth2")
Dataflow(analytics, api, "Insights", prot="OAuth2")
Dataflow(api, scm, "SCM integration", prot="HTTPS")
Dataflow(api, ims, "Inventory sync", prot="HTTPS")
Dataflow(api, tms, "Transport sync", prot="HTTPS")
Dataflow(api, wms, "Warehouse sync", prot="HTTPS")
Dataflow(api, analytics, "Control commands", prot="HTTPS")
Dataflow(analytics, actuator, "Action commands", prot="TLS")

# Process the model
tm.process()
```

# Threats

Spoofing:
- Sensor Identity Spoofing: An attacker clones or spoofs a sensor’s identity to inject false telemetry.
- RFID Tag Cloning: An adversary replicates RFID tags to misrepresent item provenance.
- GPS Signal Spoofing: Fake GPS data fed to trackers to mask real location.
- API Credential Abuse: Theft or guess of API keys to impersonate legitimate systems.
- Wireless Network Access Spoofing: Rogue access point mimics Wi‑Fi network to lure devices.

Tampering:
- Data-in-Transit Modification: Altering telemetry between IoT and edge before encryption.
- Edge Processing Injection: Malware on edge node modifies aggregated data.
- Cloud Storage Integrity Attack: Malicious insider or external attacker mutates stored IoT records.
- Actuator Command Tampering: Intercepting and changing commands en route to actuators.
- Firmware Tampering: Unauthorized modification of device firmware to change behavior.

Repudiation:
- Missing Device Logs: IoT devices lack secure logging, attackers erase traces.
- Unlogged API Access: API calls not sufficiently logged, attackers deny unauthorized actions.
- Edge Process Audit Gaps: Edge node processing lacks tamper‑proof audit trail.
- Cloud Analytics Action Denial: Lack of non‑repudiation of model‑triggered actions—difficult to prove origin.
- SCM Transaction Denial: SCM system does not cryptographically bind changes to user identity.

Information Disclosure:
- Wireless Eavesdropping: Sniffing unencrypted Bluetooth/Zigbee payloads to leak sensor data.
- Man‑in‑the‑Middle on Wi‑Fi: Intercepting TLS‑downgraded connections to extract telemetry.
- API Endpoint Data Leak: Misconfigured API exposes sensitive supply chain information.
- Cloud Storage Breach: Unauthorized access to bulk IoT data in cloud.
- Insider Data Exfiltration: Malicious cloud operator exports sensitive analytics outputs.

Denial of Service:
- Radio Jamming: Disrupting Zigbee/LoRaWAN to block sensor communication.
- Network Flooding: Flooding satellite uplink or Wi‑Fi to starve legitimate messages.
- Edge Processor Overload: Sending high‑volume fake events to crash edge node.
- Cloud API Throttling: Exhausting API request quotas to block SCM integration.
- Actuator Overload: Rapid command injections to freeze or overload actuators.

Elevation of Privilege:
- Edge OS Exploit: Vulnerability on edge device exploited to gain root.
- Container Escape in Cloud Analytics: Breaking out of container to access storage.
- Privilege Escalation via Misconfigured API: Using lax IAM roles to gain admin rights.
- SCM Application Flaw: SQL injection or logic bug granting admin SCM privileges.
- Firmware Backdoor: Malicious firmware grants hidden superuser access on IoT devices.