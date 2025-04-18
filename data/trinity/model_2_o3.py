
from pytm import TM, Boundary, Process, Dataflow, DataStore, ExternalEntity

tm = TM("Trinity Wallet")

# Boundaries
device = Boundary("Local Device")
network = Boundary("IOTA Network")

# Processes
ui = Process("User Interface", boundary=device)
twofa = Process("Two‑Factor Authentication", boundary=device)
backend = Process("Backend Logic", boundary=device)
addr_gen = Process("Address Generation", boundary=device)
tx_sign = Process("Transaction Signing", boundary=device)
node_client = Process("Node Connector", boundary=device)

# Data Stores
seed_store = DataStore("Seed Phrase Store", boundary=device, confidentiality=DataStore.C, integrity=DataStore.H)
seed_store.is_encrypted = True
history_store = DataStore("Transaction History Store", boundary=device, confidentiality=DataStore.C, integrity=DataStore.H)
history_store.is_encrypted = True

# External Entities
iota_node = ExternalEntity("IOTA Node", boundary=network)

# Data Flows
Dataflow(ui, twofa, "Initiate 2FA", confidentiality=Dataflow.C, integrity=Dataflow.C)
Dataflow(twofa, backend, "2FA result", confidentiality=Dataflow.C, integrity=Dataflow.C)

Dataflow(ui, backend, "User commands", confidentiality=Dataflow.C, integrity=Dataflow.C)
Dataflow(backend, addr_gen, "Request new address", confidentiality=Dataflow.C, integrity=Dataflow.C)
Dataflow(addr_gen, backend, "Generated address", confidentiality=Dataflow.C, integrity=Dataflow.C)

Dataflow(backend, tx_sign, "Unsigned transaction", confidentiality=Dataflow.C, integrity=Dataflow.C)
Dataflow(seed_store, tx_sign, "Seed phrase", confidentiality=Dataflow.C, integrity=Dataflow.C)
Dataflow(tx_sign, backend, "Signed transaction", confidentiality=Dataflow.C, integrity=Dataflow.C)

Dataflow(backend, node_client, "Broadcast transaction", confidentiality=Dataflow.N, integrity=Dataflow.H)
Dataflow(node_client, iota_node, "Broadcast to network", confidentiality=Dataflow.N, integrity=Dataflow.H)
Dataflow(iota_node, node_client, "Confirmation", confidentiality=Dataflow.N, integrity=Dataflow.H)
Dataflow(node_client, backend, "Confirmation", confidentiality=Dataflow.N, integrity=Dataflow.H)

Dataflow(backend, history_store, "Store transaction history", confidentiality=Dataflow.C, integrity=Dataflow.H)
Dataflow(history_store, backend, "Retrieve history", confidentiality=Dataflow.C, integrity=Dataflow.H)

tm.process()  # run analysis and output threats