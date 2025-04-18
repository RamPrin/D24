
from pytm import TM, Boundary, Actor, Server, Datastore, Process, Dataflow

tm = TM("Kubernetes Threat Model")

# Boundaries
Internet = Boundary("Internet")
Cluster = Boundary("Kubernetes Cluster")

# Actors
User = Actor("User", description="Cluster administrator or developer", boundary=Internet)
Attacker = Actor("Attacker", description="Malicious external actor", boundary=Internet)

# Components
APIserver = Server("API Server", boundary=Cluster, protocols="HTTPS", description="Kubernetes API front‑end")
etcd = Datastore("etcd", boundary=Cluster, protocols="HTTPS", description="Cluster state store")
Scheduler = Process("Scheduler", boundary=Cluster, description="Assigns pods to nodes")
ControllerMgr = Process("Controller Manager", boundary=Cluster, description="Maintains desired state")
Kubelet = Server("Kubelet", boundary=Cluster, protocols="HTTPS", description="Node agent")
KubeProxy = Process("Kube‑Proxy", boundary=Cluster, description="Service networking")
Ingress = Server("Ingress Controller", boundary=Cluster, protocols="HTTP/S", description="External HTTP routing")
Registry = Server("Container Registry", boundary=Internet, protocols="HTTPS", description="Image repository")
Pod = Process("Pod", boundary=Cluster, description="Container group")
Service = Process("Service Proxy", boundary=Cluster, description="Stable network endpoint")
ConfigMap = Datastore("ConfigMap", boundary=Cluster, description="Configuration store")
Secret = Datastore("Secret", boundary=Cluster, description="Sensitive data store")
PV = Datastore("PersistentVolume", boundary=Cluster, description="Storage resource")

# Dataflows
Dataflow(User, APIserver, "HTTPS API request", protocols="HTTPS")
Dataflow(APIserver, etcd, "Read/write cluster state", protocols="HTTPS")
Dataflow(Scheduler, APIserver, "Get pending pods", protocols="HTTPS")
Dataflow(ControllerMgr, APIserver, "Sync desired state", protocols="HTTPS")
Dataflow(Kubelet, APIserver, "Report node & pod status", protocols="HTTPS")
Dataflow(Kubelet, Registry, "Pull container images", protocols="HTTPS")
Dataflow(Ingress, Service, "Route HTTP/S traffic", protocols="HTTP/S")
Dataflow(Service, Pod, "Proxy TCP/UDP traffic", protocols="TCP/UDP")
Dataflow(Pod, PV, "Read/write storage", protocols="NFS/CSI")
Dataflow(APIserver, ConfigMap, "Deliver configuration", protocols="HTTPS")
Dataflow(APIserver, Secret, "Deliver secrets", protocols="HTTPS")

tm.process()