
from pytm import TM, Actor, Asset, Boundary, Dataflow, Server, Process, Datastore

tm = TM("Trinity Wallet Threat Model")

# Boundaries
internet = Boundary("Internet")
local_device = Boundary("Local Device")

# Actors
user = Actor("User")
iota_node = Actor("IOTA Node")

# Processes
trinity_ui = Process("Trinity Wallet UI")
trinity_ui.inBoundary = local_device

trinity_backend = Process("Trinity Wallet Backend")
trinity_backend.inBoundary = local_device

# Servers
iota_network = Server("IOTA Network")
iota_network.inBoundary = internet

# Datastores
local_storage = Datastore("Local Storage")
local_storage.inBoundary = local_device

# Assets
seed_phrase = Asset("Seed Phrase")
transaction_data = Asset("Transaction Data")

# Dataflows
ui_to_backend = Dataflow(trinity_ui, trinity_backend, "User Interactions")
backend_to_iota_network = Dataflow(trinity_backend, iota_network, "Network Interaction")
seed_storage = Dataflow(trinity_backend, local_storage, "Store Seed Phrase")
transaction_signing = Dataflow(trinity_backend, local_storage, "Sign Transaction")

# Properties
seed_phrase.stored = True
seed_phrase.encrypted = True
transaction_data.stored = True
transaction_data.encrypted = True

ui_to_backend.protocol = "local API"
backend_to_iota_network.protocol = "HTTPS"

# Trust Boundaries
internet.boundaries.append("public network")
local_device.boundaries.append("trusted device")

# Trust Assumptions
user.trusts(trinity_ui)
trinity_ui.trusts(trinity_backend)
trinity_backend.trusts(iota_network)

# Security Features
user.description = "Enables 2FA for additional security"
trinity_backend.description = "Encrypts all stored data and supports backup/recovery"

# Generate the report
tm.process()