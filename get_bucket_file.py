#!/usr/bin/env python3

import logging
import requests
from requests_auth_aws_sigv4 import AWSSigV4


logging.basicConfig() # Setup basic logging to stdout
log = logging.getLogger('requests_auth_aws_sigv4')
# log.setLevel(logging.ERROR)
log.setLevel(logging.DEBUG)

aws_service='s3'
aws_bucket='technistic-bucket'
aws_region='ap-southeast-2'
aws_object='test-bucket.txt'

aws_auth = AWSSigV4(aws_service,
    region=aws_region,
)

object_url='https://{aws_bucket}.{aws_service}.{aws_region}.amazonaws.com/{aws_object}'.format(aws_bucket=aws_bucket, aws_service=aws_service, aws_region=aws_region, aws_object=aws_object)

print('GET {object_url}'.format(object_url=object_url))
r = requests.request('GET', object_url, auth=aws_auth)
print(r.text)
