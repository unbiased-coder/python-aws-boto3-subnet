import pprint
from boto3_helper import ec2_add_subnet

result = ec2_add_subnet('vpc-af9c5bd2', '172.31.1.0/24')
pprint.pprint(result)
