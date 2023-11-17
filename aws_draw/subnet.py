from .client import client

def list_subnets_in_vpc(account, region, vpc_id):
    # Create a Boto3 client for the EC2 service
    ec2_client = client(account, 'ec2', region)

    # Use the describe_subnets method to retrieve information about subnets in the specified VPC
    response = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    subnets = {}
    for subnet in response['Subnets']:
        subnets[subnet['SubnetId']] = subnet
    return subnets

def subnets_populate(accounts):
    for description, account in accounts.items():
        for region, region_resources in account['regions'].items():
            for vpc_id in region_resources['vpcs']:
                region_resources['vpcs'][vpc_id]['subnets'] = list_subnets_in_vpc(account, region, vpc_id)
    return accounts