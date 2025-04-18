
from pytm import TM, Actor, Boundary, Process, Server, Datastore, Dataflow

tm = TM("ContactTracingApp")

# Boundaries
Device = Boundary("UserDevice")
Cloud = Boundary("CloudInfrastructure")

# Actors
User = Actor("User")
HealthAuthority = Actor("HealthAuthority")

# Components
MobileApp = Process("MobileApp")
BLEInterface = Process("BLEInterface")
GPSInterface = Process("GPSInterface")
BackendServer = Server("BackendServer")
UserDatabase = Datastore("UserDatabase")

# Assign to boundaries
Device.add(MobileApp, BLEInterface, GPSInterface)
Cloud.add(BackendServer, UserDatabase)

# Security attributes
MobileApp.localEncryption = True
MobileApp.e2eEncryption = True
BackendServer.tls = True
UserDatabase.encryptedAtRest = True

# Dataflows
Dataflow(User, MobileApp, "Register & Onboard", encryption="TLS")
Dataflow(MobileApp, BLEInterface, "Broadcast/Scan UUID")
Dataflow(BLEInterface, BLEInterface, "Exchange UUIDs", encryption="AES256")
Dataflow(MobileApp, GPSInterface, "Collect GPS Data")
Dataflow(MobileApp, BackendServer, "Upload Anonymized Logs", encryption="TLS")
Dataflow(BackendServer, UserDatabase, "Store Contact & Location Logs")
Dataflow(BackendServer, HealthAuthority, "Share Aggregated Data", encryption="TLS")

tm.process()