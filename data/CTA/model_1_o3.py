
from pytm import TM, Boundary, Process, Datastore, DataFlow

tm = TM("ContactTracingApp")

# Boundaries
mobile = Boundary("Mobile Device")
server = Boundary("Cloud Server")
health = Boundary("Health Authority")

# Components
app = Process("MobileApp", boundary=mobile)
ble = Process("BLEModule", boundary=mobile)
gps = Process("GPSModule", boundary=mobile)
storage = Datastore("LocalEncryptedStorage", boundary=mobile)
ui = Process("UserInterface", boundary=mobile)
encryption = Process("EncryptionService", boundary=mobile)

backend = Process("BackendServer", boundary=server)
database = Datastore("CentralDatabase", boundary=server)
authAPI = Process("HealthAuthAPI", boundary=server)

healthSys = Process("HealthAuthoritySystem", boundary=health)

# Dataflows
DataFlow(app, ble, "Broadcast/Scan UUID", protocol="BLE")
DataFlow(app, gps, "Collect Location", protocol="GPS")
DataFlow(app, storage, "Save Proximity & Location Logs")
DataFlow(app, backend, "Upload Encrypted Data", protocol="HTTPS")
DataFlow(backend, database, "Store Encrypted Data")
DataFlow(backend, authAPI, "Verify Positive Test", protocol="HTTPS")
DataFlow(authAPI, backend, "Test Verification Response", protocol="HTTPS")
DataFlow(backend, app, "Exposure Notification", protocol="HTTPS")

tm.process()