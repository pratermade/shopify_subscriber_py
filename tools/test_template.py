import boto3
from plumbum import cli



class TestTemplate(cli.Application):
    PROGNAME = "test_templates.py"
    VERSION = "0.1.0"

    def main(self, template, from_addr, to_addr):
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