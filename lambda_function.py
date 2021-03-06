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

def lambda_handler(event: dict, context) -> dict:
    """handles the aws lamda transaction

    Args:
        event (dict): event information
        context (_type_): aws context information

    Returns:
        dict: response dictionary
    """
    logger.info('Event: %s', event)
    event = event['detail']['payload'] # because eventbridge does it different
    data = get_data(event['email'])
    send_email(event['email'], os.environ['from_addr'], os.environ['template'], data)   
    result = "new customer {} signed up".format(event['email'])
    logger.info(result)
    response = {'result': result}
    return response


def get_data(email: str) -> str:
    """builds the data dict up for the email template

    Args:
        email (str): users email address

    Returns:
        str: the data for the email template substitution, converted to a json string
    """
    data = {
        "content": "This is a test",
        "discount_code": os.environ['DISCOUNT_CODE'],
        "username": email,
    }
    return json.dumps(data)


def send_email(emailto: str, emailfrom: str, template: str, data: dict):
    """_summary_

    Args:
        emailto (str): email address to send the email to
        emailfrom (str): email address to send the email from
        template (str): email template to use
        data (dict): data to use for the template substutions
    """
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

