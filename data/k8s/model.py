
from pytm import TM, Server, Datastore, Boundary

# Define boundaries
internet = Boundary("Internet")
cluster = Boundary("Kubernetes Cluster")

# Define components
api_server = Server("API Server")
etcd = Datastore("etcd")
controller_manager = Server("Controller Manager")
scheduler = Server("Scheduler")
kubelet = Server("Kubelet")
kube_proxy = Server("Kube-Proxy")
container_runtime = Server("Container Runtime")

# Define data stores
config_maps = Datastore("ConfigMaps")
secrets = Datastore("Secrets")
persistent_volume = Datastore("PersistentVolume")

# Assign boundaries
api_server.inBoundary = cluster
etcd.inBoundary = cluster
controller_manager.inBoundary = cluster
scheduler.inBoundary = cluster
kubelet.inBoundary = cluster
kube_proxy.inBoundary = cluster
container_runtime.inBoundary = cluster

config_maps.inBoundary = cluster
secrets.inBoundary = cluster
persistent_volume.inBoundary = cluster

# Define dataflows
from pytm import Dataflow

Dataflow(api_server, etcd, "store/retrieve configuration and state")
Dataflow(api_server, kubelet, "send pod definitions")
Dataflow(kubelet, container_runtime, "start containers")
Dataflow(kube_proxy, cluster, "manage routing and network rules")

tm = TM("Kubernetes Cluster Threat Model")
tm.process()