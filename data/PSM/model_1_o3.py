
from pytm import TM, Boundary, Actor, Process, Datastore, Dataflow

tm = TM("Password Storage Module", description="Threat model for a secure password storage component")

# Boundaries
external = Boundary("External Network")
internal = Boundary("Internal Network")

# Components
user = Actor("User", boundary=external)
auth_service = Process("AuthService", boundary=internal)
psm = Process("PasswordStorageModule", boundary=internal)
password_db = Datastore("PasswordDatabase", boundary=internal)
audit_log = Datastore("AuditLog", boundary=internal)

# Dataflows
Dataflow(user, auth_service, "Submit password", protocol="HTTPS", tls="TLS")
Dataflow(auth_service, psm, "Hash/Verify password", encryption="AES")
Dataflow(psm, password_db, "Store/Retrieve hash+salt", encryption="AES")
Dataflow(psm, audit_log, "Write audit entry", encryption="AES")

tm.process()