# Model:
```python
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
```

# Threats

Spoofing:
- FakeBLEBroadcast: A malicious device broadcasts arbitrary UUIDs to be logged as contacts. +
- RogueServerEndpoint: Attacker sets up a fake backend endpoint to collect users’ encrypted data. +
- HealthAPIImpersonation: Imposter service spoofs health authority API to inject false test verifications. -
- GPSpoofing: Malicious app or tool spoofs GPS data on the user device to falsify location logs. -

Tampering:
- TamperLocalStorage: Attacker with device access modifies or deletes stored proximity logs. +
- MITMDataModification: Man‑in‑the‑middle alters encrypted data in transit before it reaches the server. +
- AppBinaryPatching: Reverse engineering and patching the app to disable upload of positive test results. +
- DatabaseRecordAlteration: Unauthorized modification of central database entries to hide or fabricate diagnoses. -

Repudiation:
- SilentPositiveReport: User claims they never reported a positive test because no non‑repudiation log exists. +
- NotificationDenial: Server or user denies having sent or received exposure notifications without tamper‑proof logs. -
- MissingAuditTrail: Lack of immutable audit logs for data uploads and health authority confirmations. -

Information Disclosure:
- BLEEavesdropping: Attackers sniff BLE broadcasts to correlate UUIDs and re‑identify users. +
- UnencryptedLocalDump: If local storage encryption fails, proximity and location logs leak on device compromise. +
- BackendDataLeak: Central database breach exposes time‑stamped proximity records of users. +
- CorrelationAttack: Adversary combines GPS logs with other datasets to deanonymize users. -

Denial of Service:
- BLEJamming: Radio jamming to prevent devices from detecting each other. -
- ServerFlood: Flood backend API with bogus upload requests, degrading service for all users. +
- BatteryDrainAttack: Forcing continuous high‑power GPS or BLE scans to exhaust device battery. +
- StorageOverflow: Inserting excessive dummy data into local logs to exhaust device storage. +

Elevation of Privilege:
- SQLInjection: Crafting malicious input in positive test reports to execute unauthorized database commands. -
- APIPrivilegeEscalation: Exploiting unprotected endpoints to download other users’ data. +
- DebugBypass: Using rooted/jailbroken device privileges to bypass app’s privacy controls and access raw logs. -
- MisconfiguredAccessControl: Improper ACLs on cloud storage allow unauthenticated write or read of sensitive data. -