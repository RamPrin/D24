
from pytm import TM, Actor, Boundary, Server, Process, Database, DataStore, DataFlow

tm = TM("ECS Fargate Threat Model")

# Actors
developer = Actor("Developer", description="Builds and deploys container images")
attacker = Actor("Attacker", description="External adversary trying to compromise the system")

# Boundaries
aws = Boundary("AWS Cloud")
vpc = Boundary("VPC", parent=aws)
subnet = Boundary("Subnet", parent=vpc)

# Components
ecr = Server("ECR Registry", boundary=aws, description="Stores Docker images")
ecs_control = Server("ECS Control Plane", boundary=aws, description="Manages task definitions and scheduling")
fargate_task = Process("Fargate Task", boundary=aws, description="Runs containerized application")
cloudwatch = Database("CloudWatch Logs", boundary=aws, description="Ingests task logs")
iam_exec_role = DataStore("IAM Execution Role", boundary=aws, description="Grants Fargate rights to pull images and push logs")
iam_task_role = DataStore("IAM Task Role", boundary=aws, description="Grants application rights to call AWS APIs")

# Data Flows
DataFlow(developer, ecr, "Push container image", protocol="HTTPS")
DataFlow(developer, ecs_control, "Register Task Definition", protocol="HTTPS")
DataFlow(ecs_control, fargate_task, "Launch Task", protocol="HTTPS")
DataFlow(ecr, fargate_task, "Pull Docker image", protocol="HTTPS")
DataFlow(iam_exec_role, fargate_task, "Assume execution role", protocol="AWS IAM")
DataFlow(iam_task_role, fargate_task, "Assume task role", protocol="AWS IAM")
DataFlow(fargate_task, cloudwatch, "Stream logs", protocol="HTTPS")

# Potential attack path
DataFlow(attacker, ecs_control, "Malicious API calls", protocol="HTTPS")

tm.process()