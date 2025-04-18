from pytm.pytm import TM, Boundary, Server, Process, Dataflow, Data, Actor

tm = TM("Trinity Wallet Threat Model")

# Boundaries
internet = Boundary("Internet")

# Components
user = Actor("User")
ui = Process("User Interface")
backend = Server("Backend Logic")
local_storage = Data("Local Storage")
iota_network = Server("IOTA Network")
nodes = Server("Nodes")

# Dataflows
user_to_ui = Dataflow(user, ui, "User interacts with UI")
ui_to_backend = Dataflow(ui, backend, "UI communicates with Backend")
backend_to_storage = Dataflow(backend, local_storage, "Backend stores user data locally")
backend_to_iota_network = Dataflow(backend, iota_network, "Backend interacts with the IOTA network")
backend_to_nodes = Dataflow(backend, nodes, "Backend connects to nodes")
nodes_to_iota_network = Dataflow(nodes, iota_network, "Nodes validate transactions")

# Processing
tm.process()