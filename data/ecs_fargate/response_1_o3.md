# Model:
```python
from pytm import TM, Actor, Server, Dataflow, Boundary

tm = TM("ECS Fargate Threat Model")

# Boundaries
internet = Boundary("Internet")
aws_control_plane = Boundary("AWS Control Plane")
vpc = Boundary("VPC")

# Components
devops_user = Actor(
    "DevOps User",
    "Operator invoking ECS APIs to manage containers",
    boundaries=[internet]
)
aws_api = Server(
    "AWS API",
    "Entry point for ECS control plane operations",
    boundaries=[aws_control_plane]
)
ecs_control_plane = Server(
    "ECS Control Plane",
    "Manages task definitions, services, and scheduling decisions",
    boundaries=[aws_control_plane]
)
fargate_scheduler = Server(
    "Fargate Scheduler",
    "Allocates resources and launches Fargate tasks",
    boundaries=[aws_control_plane]
)
task_definition = Server(
    "Task Definition",
    "Blueprint containing container definitions and configs",
    boundaries=[aws_control_plane]
)
container_registry = Server(
    "Container Registry",
    "Stores Docker images referenced by task definitions",
    boundaries=[aws_control_plane]
)
vpc_network = Server(
    "VPC",
    "Virtual network providing isolation for Fargate tasks",
    boundaries=[vpc]
)
metadata_service = Server(
    "EC2 Metadata Service",
    "Provides IAM role credentials to running tasks",
    boundaries=[vpc]
)
cloudwatch_logs = Server(
    "CloudWatch Logs",
    "Collects and stores container logs",
    boundaries=[aws_control_plane]
)

# Dataflows
Dataflow(devops_user, aws_api, "ECS API Calls", protocols="HTTPS")
Dataflow(aws_api, ecs_control_plane, "Forward API Calls")
Dataflow(ecs_control_plane, task_definition, "Load Task Definition")
Dataflow(ecs_control_plane, fargate_scheduler, "Schedule Task Launch")
Dataflow(fargate_scheduler, container_registry, "Pull Docker Image", protocols="HTTPS")
Dataflow(fargate_scheduler, vpc_network, "Create ENI and Start Container")
Dataflow(vpc_network, metadata_service, "Fetch IAM Credentials", protocols="HTTP")
Dataflow(vpc_network, cloudwatch_logs, "Send Logs", protocols="HTTPS")

tm.process()
```

# Threats
Spoofing:
- API Request Spoofing: An attacker forges ECS API requests to AWS API to create or modify tasks. +
- Metadata Service Spoofing: A malicious container sets up a fake metadata service endpoint to harvest IAM credentials. +
- Registry Spoofing: Pulling a malicious image from a compromised or spoofed container registry. +

Tampering:
- Task Definition Tampering: Unauthorized modification of the task definition (image, environment variables, commands). +
- Container Image Tampering: Alteration of container images in the registry to include malware. +
- In‑Transit Data Tampering: Man‑in‑the‑middle altering API calls between DevOps User and AWS API or between scheduler and registry. +
- CloudWatch Log Tampering: Interception and modification or deletion of logs in transit. -

Repudiation:
- Insufficient API Logging: ECS API calls not fully logged or logs not protected, allowing an attacker to deny illicit changes. -
- Log Retention Misconfiguration: CloudWatch Logs retention settings too short or logs mutable, enabling erasure of evidence. -
- Task Execution Ambiguity: Lack of per-task audit trail preventing attribution of actions to a specific task or role. -

Information Disclosure:
- Metadata Credential Leak: Tasks using IMDSv1 may expose IAM credentials to any process inside container. +
- Sensitive Env Var Logging: Environment variables or secrets inadvertently written to CloudWatch logs. +
- Unencrypted Dataflows: Metadata service traffic over HTTP can be intercepted. +
- Excessive IAM Permissions: Over‑privileged task roles allow read access to S3 buckets, secrets, or other sensitive resources. +

Denial of Service:
- ECS API Flooding: Attackers flood ECS API with requests, exhausting rate limits and blocking legitimate operations. -
- Resource Exhaustion: Containers request excessive CPU/memory causing Fargate capacity exhaustion for other tasks. +
- Log Flooding: Tasks generate excessive logs, exhausting CloudWatch Logs ingestion quotas or storage. -
- Scheduler Overload: Rapid creation/deletion of tasks overwhelms the Fargate scheduler.

Elevation of Privilege:
- Container Escape: Exploiting a vulnerability in the Fargate runtime to gain host-level or hypervisor-level access. +
- IAM Role Escalation: Modifying task role policy to include higher‑privilege actions. +
- Service Role Misuse: Misconfigured execution role allowing tasks to assume broader AWS service roles. +
- Cross‑Task Privilege Escalation: One task accesses another task’s network namespace or metadata. -