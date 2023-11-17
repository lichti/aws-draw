import boto3

def client(account, service, region='us-east-1'):  
    # Create a session using the provided credentials
    session = boto3.Session(
        region_name=region,
        aws_access_key_id=account['access_id'],
        aws_secret_access_key=account['access_key'],
        aws_session_token=account['session_token']
    )
    
    # Create a client for the EC2 service
    client = session.client(service)
    
    return client

