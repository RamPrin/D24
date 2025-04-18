
from pytm import TM, Boundary, Actor, Process, Server, Dataflow

# Initialize Threat Model
tm = TM("Certificate Transparency")

# Boundaries
infra = Boundary("CT Infrastructure")

# Actors and Components
domain_owner = Actor("Domain Owner")
ca = Process("Certificate Authority", boundary=infra)
ct_log = Server("CT Log", boundary=infra)
monitor = Process("Monitor", boundary=infra)
auditor = Process("Auditor", boundary=infra)
client = Process("Client (Browser)", boundary=infra)

# Dataflows
Dataflow(domain_owner, ca, "Certificate Request")
Dataflow(ca, ct_log, "Submit Certificate for Logging")
Dataflow(ct_log, ca, "Signed Certificate Timestamp (SCT)")
Dataflow(ca, domain_owner, "Issued Certificate with SCT")
Dataflow(ct_log, monitor, "Log Entries Stream")
Dataflow(monitor, domain_owner, "Alerts on Suspicious Certificates")
Dataflow(auditor, ct_log, "Audit Queries")
Dataflow(ct_log, auditor, "Audit Responses")
Dataflow(client, ct_log, "SCT Inclusion Proof Request")
Dataflow(ct_log, client, "Inclusion Proof Response")

# Process the model
tm.process()