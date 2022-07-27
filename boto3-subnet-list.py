import pprint
from boto3_helper import ec2_get_subnet_list

result = ec2_get_subnet_list()
pprint.pprint(result)
