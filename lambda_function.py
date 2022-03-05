"""
Purpose

Receives notification from shopify when a new subscriber signs up and sends an email using AWS SES
"""

import logging
import boto3
import json
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
VERSION = "0.1.0"

def lambda_handler(event: dict, context):
    """
    
    """
    logger.info('Event: %s', event)
    data = get_data()

    send_email(event['email'], os.environ['from_addr'], os.environ['template'], data)
    
    result = "new customer {} signed up".format(event['email'])

    logger.info(result)

    response = {'result': result}
    return response


def get_data():
    data = {
        "content": "This is a test"
    }
    return json.dumps(data)


def send_email(emailto: str,emailfrom: str, template: str, data: dict):
    ses = boto3.client('ses')

    response = ses.send_templated_email(
    Source=emailfrom,
    Destination={
        'ToAddresses': [
        emailto,
        ],
        'CcAddresses': []
    },
    ReplyToAddresses=[
        emailfrom,
    ],
    Template=template,
    TemplateData=data
    )

    print(response)