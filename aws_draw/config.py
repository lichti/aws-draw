import configparser
from . client import client
from . regions import *
from . account import *
from . vpc import *
from . subnet import *
from . securitygroups import *
from . ec2 import *

class config:
    def __init__(self, credencials_ini='credentials.ini', settings_ini='settings.ini'):
        self.aws_accounts = self.config(credencials_ini, settings_ini)
        self.aws_accounts = vpcs_populate(self.aws_accounts)
        self.aws_accounts = subnets_populate(self.aws_accounts)
        self.aws_accounts = sg_populate(self.aws_accounts)
        self.aws_accounts = ec2_populate(self.aws_accounts)

    def config(self,credencials_ini='credentials.ini', settings_ini='settings.ini'):
        
        credentials = configparser.ConfigParser()
        credentials.read(credencials_ini)
        settings = configparser.ConfigParser()
        settings.read(settings_ini)
        
        # Organization Account
        organization_account = {
                'access_id': credentials.get(settings.get('settings', 'organization_account_section'), 'aws_access_key_id'),
                'access_key': credentials.get(settings.get('settings', 'organization_account_section'), 'aws_secret_access_key'),
                'session_token': credentials.get(settings.get('settings', 'organization_account_section'), 'aws_session_token'),
                'description': settings.get('settings', 'organization_account_section'),
                'account_id': '',
                'account_name': '',
                'regions': {}
            }
        
        # AWS accounts to check, config the credentials.ini file
        aws_accounts = {}
        
        # Iterate through each account in the credentials.ini file and set the aws_accounts dictionary
        for section in credentials.sections():
            if credentials.has_option(section, 'regions'):
                if credentials.get(section, 'regions'):
                    regions = credentials.get(section, 'regions').split(',')
            elif settings.has_option('settings', 'regions'):
                if settings.get('settings', 'regions'):
                    regions = settings.get('settings', 'regions').split(',')
            else:
                regions = []
                
            account = {
                'access_id': credentials.get(section, 'aws_access_key_id'),
                'access_key': credentials.get(section, 'aws_secret_access_key'),
                'session_token': credentials.get(section, 'aws_session_token'),
                'description': section,
                'account_id': '',
                'account_name': '',
                'regions': {},
            }
            
            if not regions:
                regions = get_all_regions(account)
                
            for region in regions:
                account['regions'][region] = {}
                
            account['account_id'] = get_id(account)
            account['account_name'] = get_name(account, organization_account)
            
            aws_accounts[section] = account
        
        return aws_accounts
