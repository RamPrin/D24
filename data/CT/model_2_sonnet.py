from pytm import TM, Server, Dataflow, Boundary, Actor, Data, DataStore, Process, Threat, Element

# Initialize the threat model
tm = TM("Certificate Transparency Security")
tm.description = "Threat model for Certificate Transparency ecosystem focusing on certificate issuance, logging, and verification"

# Define boundaries
internet = Boundary("Internet")
ca_boundary = Boundary("Certificate Authority Infrastructure")
ct_log_boundary = Boundary("CT Log Infrastructure")
domain_boundary = Boundary("Domain Owner Infrastructure")

# Define actors
domain_owner = Actor("Domain Owner")
domain_owner.inBoundary = domain_boundary

monitor = Actor("Log Monitor")
monitor.inBoundary = internet

auditor = Actor("Log Auditor")
auditor.inBoundary = internet

end_user = Actor("End User")
end_user.inBoundary = internet

attacker = Actor("Malicious Actor")
attacker.inBoundary = internet

# Define systems and processes
ca_server = Process("Certificate Authority")
ca_server.inBoundary = ca_boundary
ca_server.implementsAuthenticationScheme = True
ca_server.handlesResources = True
ca_server.hasAccessControl = True
ca_server.isHardened = True

ct_log = DataStore("Certificate Transparency Log")
ct_log.inBoundary = ct_log_boundary
ct_log.storesSensitiveData = True
ct_log.isEncrypted = True 
ct_log.isPublic = True
ct_log.isImmutable = True

domain_server = Server("Domain Web Server")
domain_server.inBoundary = domain_boundary
domain_server.usesHttps = True
domain_server.implementsAuthenticationScheme = True

browser = Process("Web Browser/Client")
browser.inBoundary = internet
browser.implementsCommunicationProtocol = "HTTPS"
browser.validatesInput = True

# Define data elements
certificate = Data("SSL/TLS Certificate", classification="Public")
certificate_request = Data("Certificate Signing Request", classification="Sensitive")
sct = Data("Signed Certificate Timestamp", classification="Public")
log_records = Data("CT Log Records", classification="Public")
domain_validation = Data("Domain Validation Data", classification="Sensitive")

# Define dataflows
df_request_cert = Dataflow(domain_owner, ca_server, "Request Certificate")
df_request_cert.protocol = "HTTPS"
df_request_cert.dstPort = 443
df_request_cert.data = certificate_request
df_request_cert.authenticatesDestination = True
df_request_cert.authenticatesSource = True

df_domain_validation = Dataflow(ca_server, domain_owner, "Validate Domain Control")
df_domain_validation.protocol = "Various (Email, DNS, HTTP)"
df_domain_validation.data = domain_validation
df_domain_validation.authenticatesDestination = True

df_ca_to_log = Dataflow(ca_server, ct_log, "Submit Certificate to Log")
df_ca_to_log.protocol = "HTTPS"
df_ca_to_log.dstPort = 443
df_ca_to_log.data = certificate
df_ca_to_log.authenticatesDestination = True

df_log_to_ca = Dataflow(ct_log, ca_server, "Return SCT")
df_log_to_ca.protocol = "HTTPS"
df_log_to_ca.data = sct
df_log_to_ca.authenticatesSource = True
df_log_to_ca.isEncrypted = True

df_ca_to_domain = Dataflow(ca_server, domain_owner, "Issue Certificate with SCT")
df_ca_to_domain.protocol = "HTTPS"
df_ca_to_domain.dstPort = 443
df_ca_to_domain.data = certificate
df_ca_to_domain.authenticatesSource = True
df_ca_to_domain.isEncrypted = True

df_monitor_to_log = Dataflow(monitor, ct_log, "Monitor Log Entries")
df_monitor_to_log.protocol = "HTTPS"
df_monitor_to_log.dstPort = 443
df_monitor_to_log.data = log_records
df_monitor_to_log.authenticatesDestination = True

df_auditor_to_log = Dataflow(auditor, ct_log, "Audit Log")
df_auditor_to_log.protocol = "HTTPS"
df_auditor_to_log.dstPort = 443
df_auditor_to_log.data = log_records
df_auditor_to_log.authenticatesDestination = True

df_user_to_domain = Dataflow(end_user, domain_server, "Visit Website")
df_user_to_domain.protocol = "HTTPS"
df_user_to_domain.dstPort = 443
df_user_to_domain.authenticatesDestination = True

df_browser_to_log = Dataflow(browser, ct_log, "Verify SCT")
df_browser_to_log.protocol = "HTTPS"
df_browser_to_log.dstPort = 443
df_browser_to_log.data = sct
df_browser_to_log.authenticatesDestination = True

tm.process()