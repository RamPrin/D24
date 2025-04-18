
from pytm import TM, Actor, Asset, Server, Dataflow, Boundary

# Define the threat model
tm = TM("IoT Supply Chain Threat Model")

# Core Components

# IoT Devices and Sensors
sensors = Asset("Sensors")
actuators = Asset("Actuators")
rfid_tags = Asset("RFID Tags")
barcodes_qr = Asset("Barcodes and QR Codes")
gps_trackers = Asset("GPS Trackers")

# Network Infrastructure
wireless_networks = Boundary("Wireless Networks")
satellite_networks = Boundary("Satellite Networks")
edge_computing = Server("Edge Computing")

# Cloud Platforms
cloud_data_storage = Asset("Cloud Data Storage")
data_analytics = Asset("Data Analytics")
api_integration = Server("API Integration")

# Software and Applications
scm_systems = Server("Supply Chain Management Systems")
inventory_management = Server("Inventory Management Systems")
tms = Server("Transportation Management Systems")
wms = Server("Warehouse Management Systems")

# Data Analytics and AI
predictive_analytics = Asset("Predictive Analytics")
machine_learning = Asset("Machine Learning")
big_data_analytics = Asset("Big Data Analytics")

# Actors
user = Actor("User")

# Dataflows
data_collection = Dataflow(user, sensors, "Data Collection")
data_transmission = Dataflow(sensors, edge_computing, "Data Transmission over Wireless Networks")
cloud_processing = Dataflow(edge_computing, cloud_data_storage, "Data Analysis and Processing in Cloud")
api_data_integration = Dataflow(cloud_data_storage, api_integration, "API Integration for SCM")

# Add boundaries
tm += wireless_networks, satellite_networks

# Key Processes
data_collection.add_dataflow_edge(user, sensors)
data_transmission.add_boundary(wireless_networks)
cloud_processing.add_dataflow_edge(edge_computing, cloud_data_storage)
api_data_integration.add_dataflow_edge(cloud_data_storage, api_integration)

# Define threats
data_security_threat = tm.add_threat(
    "Data Security",
    category="Confidentiality",
    description="Protecting sensitive data from unauthorized access.",
    exploit="Intercept Data",
)

privacy_threat = tm.add_threat(
    "Privacy",
    category="Privacy",
    description="Ensuring compliance with data protection regulations.",
    exploit="Breach Privacy",
)

interoperability_threat = tm.add_threat(
    "Interoperability",
    category="Compatibility",
    description="Ensuring compatibility between different IoT devices.",
    exploit="Disrupt Integration",
)

# Start analysis
tm.process()