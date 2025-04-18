
from pytm import TM, Boundary, Server, Dataflow, Actor

tm = TM("IoT Supply Chain Threat Model")

# Boundaries
cloud = Boundary("CloudPlatform")
edge_net = Boundary("EdgeNetwork")
wireless = Boundary("WirelessNetwork")
internet = Boundary("Internet")

# Actors
attacker = Actor("Attacker")
attacker.inBoundary = internet
user = Actor("SupplyChainUser")
user.inBoundary = internet

# IoT Devices and Gateways
sensor = Server("IoT Sensor");        sensor.inBoundary = wireless
actuator = Server("Actuator");        actuator.inBoundary = wireless
rfid    = Server("RFID Tag");         rfid.inBoundary    = wireless
gps     = Server("GPS Tracker");      gps.inBoundary     = wireless
edge_gw = Server("EdgeGateway");      edge_gw.inBoundary = edge_net

# Cloud Components
data_store = Server("DataStorage");          data_store.inBoundary = cloud
analytics  = Server("DataAnalytics");        analytics.inBoundary  = cloud
scm        = Server("SCMSystem");            scm.inBoundary        = cloud
ims        = Server("InventoryManagement");  ims.inBoundary        = cloud
tms        = Server("TransportationManagement"); tms.inBoundary    = cloud
wms        = Server("WarehouseManagement");  wms.inBoundary        = cloud

# Data Flows
Dataflow(sensor,   edge_gw, "SensorData",            prot="TLS")
Dataflow(rfid,     edge_gw, "RFIDData",              prot="TLS")
Dataflow(gps,      edge_gw, "LocationData",          prot="TLS")
Dataflow(edge_gw,  analytics, "EdgeToAnalytics",      prot="TLS")
Dataflow(analytics, data_store, "AnalyticsToStorage", prot="TLS")
Dataflow(data_store, scm,       "StorageToSCM",       prot="TLS")
Dataflow(scm,      ims,       "SCMToIMS",             prot="TLS")
Dataflow(scm,      tms,       "SCMToTMS",             prot="TLS")
Dataflow(scm,      wms,       "SCMToWMS",             prot="TLS")
Dataflow(user,     scm,       "UserToSCM",            prot="HTTPS")

# Attacker Flows
Dataflow(attacker, sensor,   "PhysicalTampering")
Dataflow(attacker, wireless, "WirelessEavesdrop",     description="Intercept unencrypted traffic")
Dataflow(attacker, edge_gw,  "GatewayCompromise",     description="Exploit vulnerabilities")
Dataflow(attacker, internet, "MITMAttack",            prot="TLS", description="Intercept/modify data")

tm.process()