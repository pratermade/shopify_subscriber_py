"""
Purpose

Receives notification from shopify when a new subscriber signs up and sends an email using AWS SES
"""

import logging
import boto3
from jinja2 import Environment, PackageLoader, select_autoescape

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: dict, context):
    """
    
    """
    logger.info('Event: %s', event)

    result = "new customer {} signed up".format(event['email'])

    logger.info(result)

    response = {'result': result}
    return response


def send_email(email: str):
    pass