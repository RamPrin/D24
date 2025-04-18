
from pytm import TM, Actor, Process, Datastore, Boundary, Dataflow

tm = TM("Certificate Transparency (CT)")

# Define boundaries
internet = Boundary("Internet")
corp_network = Boundary("Corporate Network")

# Define actors
ca = Actor("Certificate Authority", description="Trusted entities issuing SSL/TLS certificates")
monitor = Actor("Monitor", description="Checks CT logs for suspicious certificates")
auditor = Actor("Auditor", description="Verifies CA compliance with CT requirements")
client = Actor("Client (Browser)", description="Verifies certificate validity using CT info")

# Define processes
ca_process = Process("CA Process", description="Issues certificates and logs them", inBoundary=corp_network)
monitor_process = Process("Monitor Process", description="Monitors CT logs", inBoundary=corp_network)
auditor_process = Process("Auditor Process", description="Audits CT compliance", inBoundary=corp_network)
client_process = Process("Client Process", description="Validates certificate using CT", inBoundary=internet)

# Define datastores
ct_log = Datastore("CT Public Log", description="Stores all issued certificates", inBoundary=internet)

# Define dataflows
dataflow1 = Dataflow(ca, ca_process, "Certificate Issuance Request")
dataflow2 = Dataflow(ca_process, ct_log, "Log Certificate with SCT")
dataflow3 = Dataflow(monitor, monitor_process, "Monitor CT Logs")
dataflow4 = Dataflow(auditor, auditor_process, "Audit CT Compliance")
dataflow5 = Dataflow(client, client_process, "Request Certificate Validation")
dataflow6 = Dataflow(ct_log, client_process, "Provide Certificate Data")

# Define trust boundaries
dataflow1.between(ca_process, ct_log)
dataflow2.between(monitor_process, ct_log)
dataflow3.between(auditor_process, ct_log)
dataflow4.between(client_process, ct_log)

# Define the threat model properties
tm.process()