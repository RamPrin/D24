
from pytm import TM, Actor, Process, Data, Store, Boundary

tm = TM("Certificate Transparency Threat Model")

# Boundaries
internet = Boundary("Internet")
ca_boundary = Boundary("CA Infrastructure", parent=internet)
ctlog_boundary = Boundary("CT Log Infrastructure", parent=internet)
monitor_boundary = Boundary("Monitoring Infrastructure", parent=internet)
auditor_boundary = Boundary("Auditing Infrastructure", parent=internet)
client_boundary = Boundary("Client Infrastructure", parent=internet)

# Actors
domain_owner = Actor("Domain Owner", boundary=internet)
ca = Actor("Certificate Authority", boundary=ca_boundary)
monitor = Actor("Monitor", boundary=monitor_boundary)
auditor = Actor("Auditor", boundary=auditor_boundary)
client = Actor("Client", boundary=client_boundary)

# Processes
issue_cert = Process("Certificate Issuance", boundary=ca_boundary)
log_cert = Process("Logging to CT Log", boundary=ctlog_boundary)
monitor_logs = Process("Monitoring CT Logs", boundary=monitor_boundary)
audit_logs = Process("Auditing CT Logs", boundary=auditor_boundary)
validate_cert = Process("Client Certificate Validation", boundary=client_boundary)

# Store
ct_log_store = Store("CT Log Store", boundary=ctlog_boundary)

# Data flows
csr = Data("CSR", origin=domain_owner, destination=issue_cert)
raw_cert = Data("Raw Certificate", origin=issue_cert, destination=ct_log_store)
sct = Data("SCT", origin=ct_log_store, destination=issue_cert)
certificate = Data("Certificate with SCT", origin=issue_cert, destination=client)
sth = Data("STH", origin=ct_log_store, destination=validate_cert)
inclusion_request = Data("Inclusion Proof Request", origin=validate_cert, destination=ct_log_store)
inclusion_proof = Data("Inclusion Proof", origin=ct_log_store, destination=validate_cert)
alert = Data("Alert", origin=monitor_logs, destination=monitor)
audit_report = Data("Audit Report", origin=audit_logs, destination=auditor)

# Flows
domain_owner.to(issue_cert, csr)
issue_cert.to(ct_log_store, raw_cert)
ct_log_store.to(issue_cert, sct)
issue_cert.to(client, certificate)
ct_log_store.to(validate_cert, sth)
validate_cert.to(ct_log_store, inclusion_request)
ct_log_store.to(validate_cert, inclusion_proof)
ct_log_store.to(monitor_logs, raw_cert)
monitor_logs.to(monitor, alert)
ct_log_store.to(audit_logs, raw_cert)
audit_logs.to(auditor, audit_report)

tm.process()