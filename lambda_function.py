"""
Purpose

Receives notification from shopify when a new subscriber signs up and sends an email using AWS SES
"""

import logging, boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    
    """
    logger.info('Event: %s', event)

    result = "new customer {} signed up".format(event['email'])

    logger.info(result)

    response = {'result': result}
    return response
