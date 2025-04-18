
from pytm import TM, Boundary, Server, Datastore, Process, Data, Dataflow

tm = TM("Kubernetes Threat Model")

# Boundaries
internet       = Boundary("Internet")
control_plane  = Boundary("Control Plane")
worker_nodes   = Boundary("Worker Nodes")

# Control Plane Components
api_server      = Server("API Server", control_plane)
etcd            = Datastore("etcd", control_plane)
controller_mgr  = Process("Controller Manager", control_plane)
scheduler       = Process("Scheduler", control_plane)

# Worker Node Components
kubelet         = Server("Kubelet", worker_nodes)
kube_proxy      = Process("Kube-Proxy", worker_nodes)
container_rt    = Process("Container Runtime", worker_nodes)

# Data Assets
deployment_cfg  = Data("Deployment Config", source=api_server, target=etcd)
configmap_data  = Data("ConfigMap",        source=api_server, target=etcd)
secret_data     = Data("Secret",           source=api_server, target=etcd, privacy=True)
app_data        = Data("App Data",         source=container_rt, target=etcd, privacy=False)

# Data Flows
Dataflow(internet,      api_server,      "HTTPS: Kubernetes API Calls")
Dataflow(api_server,    etcd,            "gRPC/TLS: Persist Control State")
Dataflow(scheduler,     kubelet,         "gRPC/TLS: Pod Scheduling")
Dataflow(kubelet,       container_rt,    "CLI: Start Containers")
Dataflow(container_rt,  etcd,            "CSI/TLS: PV Access")
Dataflow(kube_proxy,    worker_nodes,    "iptables: Service Networking")

# Security Properties
api_server.authentication = True
api_server.protocol       = "HTTPS"
etcd.authentication       = True
etcd.encryption           = True
kubelet.authentication    = True
container_rt.trust        = "trusted_images_only"

tm.process()