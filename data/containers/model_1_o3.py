
from pytm import TM, Boundary, Server, Process, Datastore, Dataflow, ExternalEntity

# Create the threat model
tm = TM("Containerization Threat Model")

# Boundaries
host = Boundary("Host OS Boundary")
network = Boundary("Network Boundary")

# Components
developer = ExternalEntity("Developer", description="Builds and pushes container images")
container_registry = Datastore("Container Registry", description="Stores container images", boundary=network)
image_builder = Process("Image Builder", description="Builds images from Dockerfiles", boundary=host)
orchestrator = Process("Orchestrator API", description="Schedules and manages containers", boundary=host)
container_runtime = Process("Container Runtime", description="Creates and runs containers (runc/containerd)", boundary=host)
container_fs = Datastore("UnionFS Layer", description="Read-only base image + writable layers", boundary=host)
container = Process("Container", description="Isolated application runtime", boundary=host)

# Dataflows
Dataflow(developer, container_registry, "push(image)", protocols="HTTPS", auth="TLS client cert")
Dataflow(container_runtime, container_registry, "pull(image)", protocols="HTTPS", auth="TLS server cert")
Dataflow(developer, orchestrator, "deploy(cmd)", protocols="HTTPS", auth="Token")
Dataflow(orchestrator, container_runtime, "schedule(container)", protocols="gRPC", auth="mTLS")
Dataflow(container_runtime, container_fs, "read/write(layers)", protocols="Local FS")
Dataflow(container, container, "inter-container comm", protocols="Virtual Network")
Dataflow(container, network, "egress/ingress", protocols="TCP/IP", auth="None")
Dataflow(orchestrator, network, "cluster state sync", protocols="HTTPS", auth="mTLS")
Dataflow(container_runtime, host, "manage namespaces & cgroups", protocols="Kernel API", auth="root")

tm.process()