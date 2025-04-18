
from pytm import TM, Boundary, Process, DataStore, Dataflow, ExternalEntity

# Create threat model
tm = TM("PCI DSS CDE Threat Model")

# Trust boundaries
internet = Boundary("Internet")
cde = Boundary("Cardholder Data Environment")

# External entities
cardholder = ExternalEntity("Cardholder", boundary=internet)
attacker = ExternalEntity("Attacker", boundary=internet)
qsa = ExternalEntity("QSA / Assessor", boundary=internet)

# Components inside the CDE
firewall = Process("Firewall", boundary=cde)
web_app = Process("Web Application", boundary=cde)
db = DataStore("Cardholder Database", boundary=cde)
log_store = DataStore("Audit Log Store", boundary=cde)

# Data flows
Dataflow(cardholder, web_app,
         "Submit PAN over HTTPS",
         boundary=cde,
         tls=True,
         confidentiality="High",
         integrity="High")

Dataflow(web_app, db,
         "Store encrypted PAN",
         confidentiality="High",
         integrity="High")

Dataflow(web_app, log_store,
         "Write transaction log",
         confidentiality="Medium",
         integrity="High")

Dataflow(qsa, web_app,
         "Assess security controls",
         confidentiality="Low",
         integrity="Medium")

# Attacker interactions
Dataflow(attacker, web_app,
         "Attempt SQL Injection",
         authenticity="Low")

Dataflow(attacker, db,
         "Brute‑force database access",
         confidentiality="High")

# Automatically analyze threats
tm.process()