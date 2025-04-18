
from pytm import TM, Boundary, Actor, Process, DataStore, DataFlow

# Initialize threat model
tm = TM("Password Storage Module")

# Define trust boundary around the PSM
boundary_psm = Boundary("PSM Boundary")

# Actors
user = Actor("User")
attacker = Actor("Attacker")

# Processes inside the PSM
psm = Process("PSM Controller", boundary=boundary_psm)
hashing = Process("Hash & KDF", boundary=boundary_psm)
encryption = Process("Encrypt Storage", boundary=boundary_psm)

# Data stores inside the PSM
db = DataStore("Password Database", boundary=boundary_psm)
backup = DataStore("Encrypted Backup Storage", boundary=boundary_psm)

# Legitimate data flows
DataFlow(user, psm, "Submit Password", transport="TLS")
DataFlow(psm, hashing, "Salted Password")
DataFlow(hashing, encryption, "Derived Key + Hash")
DataFlow(encryption, db, "Encrypted Hash+Salt")
DataFlow(db, backup, "Encrypted Backup Snapshot")

# Attacker data flows (threats)
DataFlow(attacker, db, "Exploit DB Vulnerability")
DataFlow(attacker, backup, "Compromise Backup Storage")

# Generate the model
tm.process()