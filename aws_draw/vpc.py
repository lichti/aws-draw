from .client import client

def list_vpcs_in_region(account, region):
    # Create a Boto3 client for the EC2 service
    ec2_client = client(account, 'ec2', region)

    # Use the describe_vpcs method to retrieve information about all VPCs
    response = ec2_client.describe_vpcs()
    vpcs = {}
    for vpc in response['Vpcs']:
        vpcs[vpc['VpcId']] = vpc
    return vpcs

def vpcs_populate(accounts):
    for description, account in accounts.items():
        for region, region_resouces in account['regions'].items():
            accounts[description]['regions'][region]['vpcs'] = list_vpcs_in_region(account, region)
    return accounts