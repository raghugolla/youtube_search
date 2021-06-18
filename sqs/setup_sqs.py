#!/usr/bin/env python

import os
import sys
import boto3

sqs_endpoint_url = os.environ.get("SQS_ENDPOINT_URL")
region = os.environ.get("SQS_REGION", "ap-south-1")

print(f"creating sqs client. sqs_endpoint: {sqs_endpoint_url}")

client = boto3.client(
    "sqs",
    use_ssl=False,
    endpoint_url=sqs_endpoint_url,
    region_name=region,
    aws_access_key_id="not",
    aws_secret_access_key="relevant",
    verify=False,
)

print("creating queues")

for queue_name in sys.argv[1:]:
    response = client.create_queue(
        QueueName=queue_name, Attributes={"ReceiveMessageWaitTimeSeconds": "10"}
    )

print("Done creating sqs queues")

exit(0)
