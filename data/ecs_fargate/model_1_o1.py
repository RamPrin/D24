
from pytm import *

tm = TM("ECS Fargate Threat Model")

# Boundaries
internet = Boundary("Internet")
aws_cloud = Boundary("AWS Cloud")

# Components
container_definition = Server("Container Definition")
task_definition = Server("Task Definition")
ecs_service = Server("ECS Service/Task")
ecs_cluster = Server("ECS Cluster")
vpc = Boundary("VPC")
iam_role = Server("IAM Roles")
logging = Server("Logging to CloudWatch")

# Dataflows
df1 = Dataflow(internet, container_definition, "Container Configuration")
df2 = Dataflow(container_definition, task_definition, "Task Blueprint")
df3 = Dataflow(task_definition, ecs_service, "Run Tasks/Services")
df4 = Dataflow(ecs_service, ecs_cluster, "Manage Services/Tasks")
df5 = Dataflow(ecs_service, vpc, "Network Traffic")
df6 = Dataflow(ecs_service, iam_role, "IAM Role Access")
df7 = Dataflow(ecs_service, logging, "Log Data")
df8 = Dataflow(logging, aws_cloud, "Log Storage")

tm.process()