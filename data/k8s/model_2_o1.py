
from pytm import TM, Actor, Boundary, Process, DataStore, DataFlow, Server

# Define the threat model
tm = TM("Kubernetes Threat Model")

# Define actors
malicious_insider = Actor("Malicious Insider")
external_attacker = Actor("External Attacker")

# Define boundaries
kubernetes_cluster = Boundary("Kubernetes Cluster")
network_boundary = Boundary("Network Boundary")
etcd_boundary = Boundary("Etcd Boundary")

# Define processes
api_server = Process("API Server", parent=kubernetes_cluster)
scheduler = Process("Scheduler", parent=kubernetes_cluster)
controller_manager = Process("Controller Manager", parent=kubernetes_cluster)
kubelet = Process("Kubelet", parent=kubernetes_cluster)
kube_proxy = Process("Kube-Proxy", parent=kubernetes_cluster)
container_runtime = Process("Container Runtime", parent=kubernetes_cluster)

# Define data stores
etcd = DataStore("etcd", parent=etcd_boundary)
config_data = DataStore("ConfigMaps & Secrets", parent=kubernetes_cluster)
app_data = DataStore("PersistentVolumes", parent=kubernetes_cluster)

# Define data flows
df1 = DataFlow(malicious_insider, api_server, "Exploit misconfigured RBAC")
df2 = DataFlow(external_attacker, etcd, "Exploit weak authentication")
df3 = DataFlow(external_attacker, api_server, "Network interception")

# Define servers and network
kube_master = Server("Kubernetes Master Node", parent=kubernetes_cluster)
kube_worker = Server("Kubernetes Worker Node", parent=kubernetes_cluster)

# Define threats and mitigations
api_server.threats.append("Unauthorized access", methods=["Implement strict RBAC"])
etcd.threats.append("Data breach", methods=["Use strong authentication, enable TLS"])
network_boundary.threats.append("Man-in-the-middle attack", methods=["Enable TLS, network segmentation"])

# Generate the threat model
tm.process()