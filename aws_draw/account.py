from .client import client
import botocore

def get_id(account):
    sts_client = client(account, 'sts')
    account_id = sts_client.get_caller_identity().get('Account')
    return account_id

def get_name(account, organization_account):
    org_client = client(organization_account, 'organizations')
    try:
        account_name = org_client.describe_account(AccountId=account['account_id']).get('Account').get('Name')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'AccessDeniedException':
            account_name=account['account_id']
        else:
            raise e
    return account_name


# # AWS Organizations Account client to get the accounts names
# organizations_client = boto3.client(
#     'organizations',
#     aws_access_key_id=aws_accounts[aws_organization_account]['access_id'],
#     aws_secret_access_key=aws_accounts[aws_organization_account]['access_key'],
#     aws_session_token=aws_accounts[aws_organization_account]['session_token']
# )

# # Get the account name
# # If the account does not have permission to get the account name, it will print only the account id
# try:
#     account_name = organizations_client.describe_account(AccountId=account_id).get('Account').get('Name')
#     print(f"Account name: {account_name} ({account_id})")
# except botocore.exceptions.ClientError as e:
#     if e.response['Error']['Code'] == 'AccessDeniedException':
#         print(f"Account ({account_id}) - Access denied to get Account Name")
#     else:
#         raise e

    
