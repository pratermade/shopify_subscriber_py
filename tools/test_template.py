import boto3
from plumbum import cli

"""Sends a test email"""


class TestTemplate(cli.Application):
    PROGNAME = "test_templates.py"
    VERSION = "0.1.0"

    def main(self, template: str, from_addr: str, to_addr: str) -> int:
        """sends an email to the specified address

        Args:
            template (str): template for the email
            from_addr (str): the address to send from
            to_addr (str): the address to send to

        Returns:
            int: return code
        """
        ses = boto3.client('ses')

        response = ses.send_templated_email(
        Source= from_addr,
        Destination={
            'ToAddresses': [
            to_addr,
            ],
            'CcAddresses': []
        },
        ReplyToAddresses=[
            from_addr,
        ],
        Template=template,
        TemplateData='''{ "content":"This is some test contents" }'''
        )

        print(response)

if __name__== "__main__":
    TestTemplate.run()