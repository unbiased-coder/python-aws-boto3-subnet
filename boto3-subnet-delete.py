import pprint
from boto3_helper import ec2_delete_subnet

result = ec2_delete_subnet('subnet-0604756b09f4a2dcd')
pprint.pprint(result)