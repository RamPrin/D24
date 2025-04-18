
from pytm import TM, Boundary, Server, Dataflow, Actor, Data

tm = TM("PCI DSS Compliance Model")

# Boundaries
cde_boundary = Boundary("Cardholder Data Environment (CDE)")

# Components
firewall = Server("Firewall")
firewall.inBoundary = cde_boundary

database_server = Server("Database Server")
database_server.inBoundary = cde_boundary

application_server = Server("Application Server")
application_server.inBoundary = cde_boundary

antivirus = Server("Antivirus Solution")
antivirus.inBoundary = cde_boundary

admin_user = Actor("Admin User")

# Data
cardholder_data = Data("Cardholder Data")
cardholder_data.inBoundary = cde_boundary
cardholder_data.isPII = True

# Dataflows
df1 = Dataflow(admin_user, firewall, "Configure Firewall")
df2 = Dataflow(application_server, database_server, "Store Cardholder Data")
df2.data = cardholder_data
df3 = Dataflow(database_server, application_server, "Fetch Cardholder Data")
df3.data = cardholder_data
df4 = Dataflow(application_server, firewall, "Transmit Encrypted Data")
df4.data = cardholder_data
df5 = Dataflow(antivirus, database_server, "Scan for Threats")

tm.process()