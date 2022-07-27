import os
import boto3
import pprint
from dotenv import load_dotenv

def get_aws_keys():
    load_dotenv()
    return os.getenv('AWS_ACCESS_KEY'), os.getenv('AWS_SECRET_KEY')

def init_aws_session():
    access_key, secret_key = get_aws_keys()
    return boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=os.getenv('AWS_REGION'))

def ec2_get_subnet_list():
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.describe_subnets()
    return response['Subnets']

def ec2_add_subnet(vpc_id, ip_block):
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.create_subnet(VpcId=vpc_id, CidrBlock=ip_block)
    return response['Subnet']

def ec2_delete_subnet(subnet_id):
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.delete_subnet(SubnetId=subnet_id)
    return response


