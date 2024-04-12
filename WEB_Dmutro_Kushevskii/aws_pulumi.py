import pulumi
import pulumi_aws as aws

# Create an ECS cluster
cluster = aws.ecs.Cluster("app-cluster")

# Create a VPC for the ECS cluster
vpc = aws.ec2.Vpc("app-vpc", cidr_block="10.0.0.0/16")

# Create a security group for the ECS tasks
security_group = aws.ec2.SecurityGroup("app-security-group",
    vpc_id=vpc.id,
    ingress=[{
        "protocol": "tcp",
        "from_port": 80,
        "to_port": 80,
        "cidr_blocks": ["0.0.0.0/0"],
    }],
)

# Create a task definition for the FastAPI application
task_definition = aws.ecs.TaskDefinition("app-task",
    container_definitions="""[
        {
            "name": "app-container",
            "image": "tiangolo/uvicorn-gunicorn-fastapi:python3.8",
            "portMappings": [
                {
                    "containerPort": 80,
                    "hostPort": 80,
                    "protocol": "tcp"
                }
            ]
        }
    ]""",
)

# Create a service to run the task on the ECS cluster
service = aws.ecs.Service("app-service",
    cluster=cluster.arn,
    task_definition=task_definition.arn,
    desired_count=1,
    launch_type="FARGATE",
    network_configuration={
        "assign_public_ip": True,
        "subnets": aws.ec2.get_subnet_ids(vpc_id=vpc.id).ids,
        "security_groups": [security_group.id],
    },
)