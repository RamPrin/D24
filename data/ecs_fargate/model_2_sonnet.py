from pytm import TM, Server, Dataflow, Boundary, Actor, Data, DataStore, Process, Threat, Element

# Initialize the threat model
tm = TM("AWS ECS Fargate Security")
tm.description = "Threat model for AWS ECS Fargate focusing on container orchestration, networking, and task execution"

# Define boundaries
aws_cloud = Boundary("AWS Cloud")
vpc = Boundary("Virtual Private Cloud", parent=aws_cloud)
fargate_platform = Boundary("Fargate Platform", parent=aws_cloud)
container_runtime = Boundary("Container Runtime", parent=fargate_platform)
aws_management = Boundary("AWS Management Plane")

# Define actors
cloud_admin = Actor("Cloud Administrator")
cloud_admin.inBoundary = aws_management

application_developer = Actor("Application Developer")
application_developer.inBoundary = aws_management

end_user = Actor("End User")
end_user.inScope = True

attacker = Actor("Malicious Actor")
attacker.inScope = True

# Define systems and processes
ecs_control_plane = Process("ECS Control Plane")
ecs_control_plane.inBoundary = aws_cloud
ecs_control_plane.implementsAuthenticationScheme = True
ecs_control_plane.hasAccessControl = True

task_orchestrator = Process("Task Orchestrator")
task_orchestrator.inBoundary = fargate_platform
task_orchestrator.implementsAuthenticationScheme = True
task_orchestrator.hasAccessControl = True

container_agent = Process("Container Agent")
container_agent.inBoundary = container_runtime
container_agent.implementsAuthenticationScheme = True

task_execution = Process("Task Execution")
task_execution.inBoundary = container_runtime
task_execution.implementsAuthenticationScheme = True
task_execution.hasAccessControl = True

application_container = Process("Application Container")
application_container.inBoundary = container_runtime
application_container.handlesResources = True
application_container.implementsAuthenticationScheme = False

ecr_registry = DataStore("ECR Container Registry")
ecr_registry.inBoundary = aws_cloud
ecr_registry.isEncrypted = True
ecr_registry.storesSensitiveData = True

secrets_manager = DataStore("AWS Secrets Manager")
secrets_manager.inBoundary = aws_cloud
secrets_manager.isEncrypted = True
secrets_manager.storesSensitiveData = True

cloudwatch_logs = DataStore("CloudWatch Logs")
cloudwatch_logs.inBoundary = aws_cloud
cloudwatch_logs.storesSensitiveData = True
cloudwatch_logs.isEncrypted = True

load_balancer = Process("Application Load Balancer")
load_balancer.inBoundary = vpc
load_balancer.implementsAuthenticationScheme = False
load_balancer.validatesInput = True

# Define data elements
container_image = Data("Container Image", classification="Internal")
task_definition = Data("Task Definition", classification="Sensitive")
container_secrets = Data("Container Secrets/Env Vars", classification="Secret")
application_data = Data("Application Data", classification="Sensitive")
task_role_credentials = Data("Task Role Credentials", classification="Secret")
log_data = Data("Container Logs", classification="Internal")
user_requests = Data("User Requests", classification="Internal")
user_responses = Data("Application Responses", classification="Internal")

# Define dataflows
df_admin_ecs = Dataflow(cloud_admin, ecs_control_plane, "Configure ECS Service/Tasks")
df_admin_ecs.protocol = "HTTPS"
df_admin_ecs.dstPort = 443
df_admin_ecs.data = task_definition
df_admin_ecs.isEncrypted = True
df_admin_ecs.authenticatesSource = True
df_admin_ecs.authenticatesDestination = True

df_deploy_image = Dataflow(application_developer, ecr_registry, "Push Container Image")
df_deploy_image.protocol = "HTTPS"
df_deploy_image.dstPort = 443
df_deploy_image.data = container_image
df_deploy_image.isEncrypted = True
df_deploy_image.authenticatesSource = True

df_ecs_orchestrator = Dataflow(ecs_control_plane, task_orchestrator, "Launch Task")
df_ecs_orchestrator.protocol = "AWS Internal"
df_ecs_orchestrator.data = task_definition
df_ecs_orchestrator.isEncrypted = True
df_ecs_orchestrator.authenticatesSource = True
df_ecs_orchestrator.authenticatesDestination = True

df_orchestrator_agent = Dataflow(task_orchestrator, container_agent, "Configure Container")
df_orchestrator_agent.protocol = "AWS Internal"
df_orchestrator_agent.data = task_definition
df_orchestrator_agent.isEncrypted = True
df_orchestrator_agent.authenticatesSource = True
df_orchestrator_agent.authenticatesDestination = True

df_pull_image = Dataflow(container_agent, ecr_registry, "Pull Container Image")
df_pull_image.protocol = "HTTPS"
df_pull_image.dstPort = 443
df_pull_image.data = container_image
df_pull_image.isEncrypted = True
df_pull_image.authenticatesSource = True
df_pull_image.authenticatesDestination = True

df_get_secrets = Dataflow(task_execution, secrets_manager, "Retrieve Secrets")
df_get_secrets.protocol = "HTTPS"
df_get_secrets.dstPort = 443
df_get_secrets.data = container_secrets
df_get_secrets.isEncrypted = True
df_get_secrets.authenticatesSource = True
df_get_secrets.authenticatesDestination = True

df_start_container = Dataflow(container_agent, application_container, "Start Container")
df_start_container.protocol = "Container Runtime API"
df_start_container.data = [container_image, container_secrets]
df_start_container.isEncrypted = True

df_container_logs = Dataflow(application_container, cloudwatch_logs, "Send Logs")
df_container_logs.protocol = "HTTPS"
df_container_logs.dstPort = 443
df_container_logs.data = log_data
df_container_logs.isEncrypted = True
df_container_logs.authenticatesDestination = True

df_user_request = Dataflow(end_user, load_balancer, "User Request")
df_user_request.protocol = "HTTPS"
df_user_request.dstPort = 443
df_user_request.data = user_requests
df_user_request.isEncrypted = True
df_user_request.isPublicNetwork = True
df_user_request.authenticatesDestination = True

df_lb_container = Dataflow(load_balancer, application_container, "Forward Request")
df_lb_container.protocol = "HTTP/HTTPS"
df_lb_container.data = user_requests
df_lb_container.isEncrypted = True

df_container_response = Dataflow(application_container, load_balancer, "Application Response")
df_container_response.protocol = "HTTP/HTTPS"
df_container_response.data = user_responses
df_container_response.isEncrypted = True

df_response_user = Dataflow(load_balancer, end_user, "Return Response")
df_response_user.protocol = "HTTPS"
df_response_user.data = user_responses
df_response_user.isEncrypted = True
df_response_user.isPublicNetwork = True

df_metadata_service = Dataflow(application_container, task_execution, "Request Credentials")
df_metadata_service.protocol = "AWS Internal"
df_metadata_service.data = task_role_credentials
df_metadata_service.isEncrypted = True

tm.process()