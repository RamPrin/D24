
from pytm import TM, Actor, Process, DataStore, DataFlow, Boundary

# Define threat model
tm = TM("Password Storage Module")

# Actors
user = Actor("User")
admin = Actor("Admin")

# Components
psm = Process("Password Storage Module")
hashing_algorithm = Process("Hashing Algorithm")
database = DataStore("Secure Database")
backup_storage = DataStore("Backup Storage")
logging_system = DataStore("Audit Logs")

# Data flows
user_credentials = DataFlow(user, psm, "User Credentials")
hashing_process = DataFlow(psm, hashing_algorithm, "Password with Salt")
hashed_password = DataFlow(hashing_algorithm, database, "Hashed Password & Salt")
database_access = DataFlow(admin, database, "Admin Access")
logging_access = DataFlow(admin, logging_system, "Access & Modification Logs")
backup_creation = DataFlow(database, backup_storage, "Secure Backups")

# Boundaries
network_boundary = Boundary("Network Boundary")
storage_boundary = Boundary("Storage Boundary")

# Link elements to boundaries
psm.inBoundary = network_boundary
database.inBoundary = storage_boundary
backup_storage.inBoundary = storage_boundary
logging_system.inBoundary = storage_boundary

# Trust assumptions
psm.assumptions.append("Authentication ensures authorized access only")
database.assumptions.append("Encrypted at rest and in transit")
logging_system.assumptions.append("Tamper-proof audit logs")

# Set data attributes
user_credentials.data = "Username, Password"
hashed_password.data = "Hashed Password with Salt"
backup_creation.data = "Encrypted Data Backup"

# Define the view
tm.process()