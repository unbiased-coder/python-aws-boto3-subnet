import pprint
from boto3_helper import ec2_delete_subnet

result = ec2_delete_subnet('subnet-0128e4cd0a6ebca54')
pprint.pprint(result)