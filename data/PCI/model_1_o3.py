
from pytm import TM, Boundary, Actor, Server, DataFlow, DataStore

tm = TM("PCI DSS Compliance Environment")

# Boundaries
b_external = Boundary("External Network")
b_cde      = Boundary("Cardholder Data Environment")
b_internal = Boundary("Internal Corporate Network")
b_qsa      = Boundary("QSA Boundary")

# Actors
cardholder = Actor("Cardholder", boundary=b_external)
merchant   = Actor("Merchant Staff", boundary=b_internal)
qsa        = Actor("Qualified Security Assessor", boundary=b_qsa)
bank       = Actor("Acquiring Bank", boundary=b_external)

# Components
web_server   = Server("Web Server", boundary=b_external)
app_server   = Server("Application Server", boundary=b_cde)
db_server    = Server("Database Server", boundary=b_cde)
log_store    = DataStore("Log Store", boundary=b_internal)
siem         = Server("SIEM", boundary=b_internal)
assessment   = Server("Self‐Assessment System", boundary=b_internal)
roc_store    = DataStore("RoC Repository", boundary=b_qsa)

# Dataflows
DataFlow(cardholder, web_server,   "Submit Payment Details",       protocols="HTTPS")
DataFlow(web_server, app_server,   "Forward Payment Request",      protocols="Internal API")
DataFlow(app_server, db_server,    "Query/Store Cardholder Data",  protocols="Encrypted DB")
DataFlow(app_server, log_store,    "Write Transaction Logs",        protocols="TLS")
DataFlow(log_store, siem,          "Log Forwarding",               protocols="Syslog/TLS")
DataFlow(merchant, assessment,     "Upload Self‐Assessment Data",  protocols="HTTPS")
DataFlow(assessment, qsa,          "Send Assessment Reports",      protocols="SFTP")
DataFlow(qsa, roc_store,           "Store Validated RoC",          protocols="SFTP")
DataFlow(roc_store, bank,          "Submit RoC to Bank",           protocols="SFTP")

tm.process()