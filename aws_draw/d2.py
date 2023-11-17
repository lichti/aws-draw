from py_d2 import *
from . vpc import *

class D2:
    def __init__(self, accounts):
        self.shapes = []
        self.connections = []
        self.make(accounts)
        self.draw()

    def draw(self):
        diagram = D2Diagram(shapes=self.shapes, connections=self.connections)
        with open("graph.d2", "w", encoding="utf-8") as f:
            f.write(str(diagram))
            
    def make(self, accounts):
        for account, account_res in accounts.items():
            print("ACCOUTN=====================")
            print(account_res)
            account_shape = D2Shape(
                name=account_res['account_id'],
                #type="rectangle",
                label=account_res['account_name'],
            )
            for region, region_res in account_res['regions'].items():
                print("REGION=====================")
                print(region_res)
                region_shape=D2Shape(
                    name=region,
                    #type="rectangle",
                    label=region,
                )
                for vpc, vpc_res in region_res['vpcs'].items():
                    print("VPC=====================")
                    print(vpc_res)
                    vpc_shape = D2Shape(
                        name=vpc_res['VpcId'],
                        #type="rectangle",
                        label=vpc_res['CidrBlock'],
                    )
                    for subnet, subnet_res in vpc_res['subnets'].items():
                        print("SUBNET=====================")
                        print(subnet_res)
                        subnet_shape = D2Shape(
                            name=subnet_res['SubnetId'],
                            #type="rectangle",
                            label=subnet_res['CidrBlock'],
                        )
                        vpc_shape.add_shape(subnet_shape)
                        for ec2_res in subnet_res['ec2_instances']:
                            print("EC2=====================")
                            print(ec2_res)
                            ec2_shape = D2Shape(
                                name=ec2_res['InstanceId'],
                                #type="rectangle",
                                label=ec2_res['PrivateIpAddress'],
                            )
                            subnet_shape.add_shape(ec2_shape)
                    # for sg, sg_res in vpc_res['security_groups'].items():
                    #     print("SG=====================")
                    #     print(sg_res)
                    #     sg_shape = D2Shape(
                    #         name=sg_res['GroupId'],
                    #         #type="rectangle",
                    #         label=sg_res['GroupName'],
                    #     )
                    #     vpc_shape.add_shape(sg_shape)
                    region_shape.add_shape(vpc_shape)
                account_shape.add_shape(region_shape)
            self.shapes.append(account_shape)
