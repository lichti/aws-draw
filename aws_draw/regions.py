from . client import client
import boto3

def get_all_regions(account):
    # Create a client for the EC2 service
    ec2_client = client(account, 'ec2')
    
    # Get all the regions using the client
    response = ec2_client.describe_regions()
    regions = [region['RegionName'] for region in response['Regions']]
    
    return regions