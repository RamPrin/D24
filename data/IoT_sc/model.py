from pytm import TM, Actor, Boundary, Dataflow, Server, Data, Process

# Define the threat model
tm = TM("IoT Supply Chain Management")

# Boundaries
internet = Boundary("Internet")
enterprise_network = Boundary("Enterprise Network")
cloud = Boundary("Cloud")

# Components
iot_devices = Actor("IoT Devices and Sensors")
network_infrastructure = Server("Network Infrastructure")
cloud_platforms = Server("Cloud Platforms")
scm_system = Server("Supply Chain Management Systems")
data_analytics = Process("Data Analytics and AI")

# Dataflows
df1 = Dataflow(iot_devices, network_infrastructure, "Data Collection")
df2 = Dataflow(network_infrastructure, cloud_platforms, "Data Transmission")
df3 = Dataflow(cloud_platforms, data_analytics, "Data Processing")
df4 = Dataflow(data_analytics, scm_system, "Decision Making")
df5 = Dataflow(scm_system, iot_devices, "Action Execution")

# Set boundaries
iot_devices.inBoundary = internet
network_infrastructure.inBoundary = enterprise_network
cloud_platforms.inBoundary = cloud
scm_system.inBoundary = enterprise_network
data_analytics.inBoundary = cloud

# Data
data = Data("IoT Data")
data.inBoundary = cloud
data.process = data_analytics

tm.process()