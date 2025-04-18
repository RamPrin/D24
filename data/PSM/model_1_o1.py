
from pytm import TM, Server, Dataflow, Boundary, Actor, Datastore, Process

# Define boundaries
internal_boundary = Boundary(name="Internal Network")

# Define components
user = Actor(name="User")
password_storage = Datastore(name="Password Storage", in_boundary=internal_boundary)
auth_mechanism = Process(name="Authentication Mechanism", in_boundary=internal_boundary)
hashing_process = Process(name="Hashing Process", in_boundary=internal_boundary)

# Define dataflows
user_input_flow = Dataflow(name="User Input", source=user, destination=auth_mechanism)
password_hash_flow = Dataflow(name="Password Hash Flow", source=hashing_process, destination=password_storage)
verification_flow = Dataflow(name="Password Verification", source=auth_mechanism, destination=password_storage)

# Initialize and process the threat model
tm = TM("Password Storage Module Threat Model")
tm += [user, password_storage, auth_mechanism, hashing_process, user_input_flow, password_hash_flow, verification_flow]
tm.process()