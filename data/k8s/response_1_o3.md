# Model:
```python
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
```

# Threats

Spoofing:
- API Server Impersonation: Attacker forges API requests to the API Server.
- Node Identity Spoofing: Malicious host pretends to be a legitimate node to join the cluster.
- Kubelet Impersonation: Unauthorized actor masquerades as a Kubelet to report bogus status.
- etcd Client Spoofing: Attacker fakes etcd client identity to read/write state.
- Ingress Host Spoofing: Malicious endpoint impersonates an Ingress to intercept traffic.

Tampering:
- etcd Data Tampering: Unauthorized modification of cluster state in etcd.
- ConfigMap Tampering: Attacker alters ConfigMap entries to change application behavior.
- Secret Tampering: Unauthorized modification of secrets stored in the cluster.
- Container Image Tampering: Malicious registry injects trojanized images.
- API Request Tampering: Man-in-the-middle modifies API payloads in transit.
- PersistentVolume Tampering: Unauthorized alteration of data on PVs.

Repudiation:
- API Audit Log Deletion: Attacker erases or alters audit logs stored in etcd.
- Kubelet Report Repudiation: Node denies sending false pod status reports.
- Controller Action Repudiation: Malicious controller changes state and denies it.
- Config Change Repudiation: Users deny having applied configuration updates without proof.

Information Disclosure:
- etcd Data Exposure: Unauthorized read of etcd exposes secrets and configs.
- Secret Leakage via Logs: Secrets accidentally logged by API Server or Kubelet.
- Network Sniffing of Pod Traffic: Eavesdropping on unencrypted pod communications.
- Container Image Metadata Exposure: Sensitive info in image layers leaked.
- PersistentVolume Data Exposure: Unauthorized access to PV data.
- Ingress Header Leakage: Sensitive headers exposed in HTTP ingress logs.

Denial of Service:
- API Server DoS: Flooding API endpoints to exhaust resources.
- etcd DoS: Overwhelming etcd with requests to slow cluster operations.
- Scheduler Queue Flooding: Submitting many pods to block scheduling.
- Kubelet Resource Exhaustion: Flooding kubelet with status updates.
- Registry Bandwidth Exhaustion: Excessive image pulls degrade performance.
- Network Flooding: DDoS on cluster network interfaces.
- PV Capacity Exhaustion: Filling PV storage to prevent writes.

Elevation of Privilege:
- RBAC Misconfiguration: Attacker gains cluster-admin via overly permissive roles.
- Privileged Pod Creation: User deploys privileged pod to access host.
- Node Escalation via Container Runtime: Exploit container runtime to gain host root.
- API Server Vulnerability Exploit: Use unpatched bug to gain admin rights.
- Controller Manager Exploit: Elevate to cluster-admin through controller flaw.
- etcd ACL Bypass: Circumvent etcd access controls to gain write privileges.