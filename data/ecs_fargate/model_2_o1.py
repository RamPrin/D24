
from pytm import TM, Server, Datastore, Actor, Boundary, Dataflow

# Define the threat model
ecs_fargate_tm = TM("ECS Fargate Threat Model")

# Define boundaries
internet = Boundary("Internet")
vpc = Boundary("VPC")

# Define elements
user = Actor("User")

ecs_cluster = Server("ECS Cluster")
ecs_cluster.inBoundary = vpc

container_definition = Datastore("Container Definition")
container_definition.inBoundary = vpc

task_definition = Datastore("Task Definition")
task_definition.inBoundary = vpc

service_task = Server("Service/Task")
service_task.inBoundary = vpc

cloudwatch_logs = Datastore("CloudWatch Logs")
cloudwatch_logs.inBoundary = Boundary("AWS Cloud")

# Define dataflows
user_to_cluster = Dataflow(user, ecs_cluster, "User requests to ECS Cluster")

cluster_to_service_task = Dataflow(ecs_cluster, service_task, "ECS Cluster manages tasks/services")

service_task_to_container_definition = Dataflow(service_task, container_definition, "Service/Task uses Container Definition")

service_task_to_task_definition = Dataflow(service_task, task_definition, "Service/Task uses Task Definition")

service_task_to_logs = Dataflow(service_task, cloudwatch_logs, "Service/Task logs to CloudWatch")

# Define network isolation
ecs_fargate_tm.networkBoundary = vpc

# Define IAM roles and privileges
iam_roles = Datastore("IAM Roles")
iam_roles.inBoundary = Boundary("IAM System")

ecs_task_to_iam_roles = Dataflow(service_task, iam_roles, "Task assumes IAM Role")

# Define VPC security
vpc_security_groups = Datastore("VPC Security Groups")
vpc_security_groups.inBoundary = vpc

vpc_subnets = Datastore("VPC Subnets")
vpc_subnets.inBoundary = vpc

ecs_fargate_tm.process()