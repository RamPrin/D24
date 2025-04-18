
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