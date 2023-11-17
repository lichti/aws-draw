from .client import client

def list_ec2_instances_in_subnet(account, region, subnet_id):
    # Create a Boto3 client for the EC2 service
    ec2_client = client(account, 'ec2', region)

    # Use the describe_instances method to retrieve information about EC2 instances in the specified subnet
    response = ec2_client.describe_instances(Filters=[{'Name': 'subnet-id', 'Values': [subnet_id]}])
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    return instances

def ec2_populate(accounts):
    for description, account in accounts.items():
        for region, region_resources in account['regions'].items():
            for vpc_id in region_resources['vpcs']:
                for subnet_id in region_resources['vpcs'][vpc_id]['subnets']:
                    region_resources['vpcs'][vpc_id]['subnets'][subnet_id]['ec2_instances'] = list_ec2_instances_in_subnet(account, region, subnet_id)
    return accounts