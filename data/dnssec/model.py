
from pytm.pytm import TM, Server, Datastore, Dataflow, Boundary, Actor

# Define the threat model
tm = TM("DNSSEC Threat Model")

# Define boundaries
public_network = Boundary("Public Network")
dns_zone = Boundary("DNS Zone")

# Define components
client = Actor("Client")
dns_server = Server("DNS Server")
zone_admin = Actor("Zone Administrator")
dns_datastore = Datastore("DNS Datastore")

# Adding components to boundaries
client.inBoundary = public_network
dns_server.inBoundary = dns_zone
zone_admin.inBoundary = dns_zone
dns_datastore.inBoundary = dns_zone

# Define dataflows
df1 = Dataflow(zone_admin, dns_datastore, "Publish DNS Records")
df2 = Dataflow(client, dns_server, "Query DNS Record")
df3 = Dataflow(dns_server, client, "Return DNS Record")
df4 = Dataflow(dns_server, dns_datastore, "Authenticate DNS Record")

# Process the threat model
tm.process()