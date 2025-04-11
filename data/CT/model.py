
from pytm import TM, Server, Datastore, Dataflow, Actor, Boundary

# Define the threat model
tm = TM("Certificate Transparency")

# Define boundaries
internet = Boundary("Internet")
ca_boundary = Boundary("Certificate Authority Boundary")
log_boundary = Boundary("CT Log Boundary")

# Define external elements
client = Actor("Browser/Client")
domain_owner = Actor("Domain Owner")

# Define internal components
ca = Server("Certificate Authority")
ct_log = Datastore("Public CT Log")
monitor = Server("Monitor")
auditor = Server("Auditor")

# Define dataflows
Dataflow(domain_owner, ca, "Certificate Request")
Dataflow(ca, ct_log, "Log Certificate")
Dataflow(ca, domain_owner, "Issue Certificate with SCT")
Dataflow(ct_log, client, "Verify Certificate")
Dataflow(monitor, ct_log, "Monitor Logs")
Dataflow(auditor, ct_log, "Audit Logs")
Dataflow(client, ct_log, "Certificate Validation")

tm.process()