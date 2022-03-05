
import boto3
import sys
import os
from plumbum import cli



class ManageTemplates(cli.Application):
    PROGNAME = "manage_templates.py"
    VERSION = "0.1.0"

    def main(self, *args):
        if args:
            print(f"Unknown Command {args[0]}")
        if not self.nested_command:
            print("no command given")
            return 1

@ManageTemplates.subcommand("update")
class UpdateTemplate(cli.Application):
    DESCRIPTION = "update the template on aws"
    def main(self, templatename):
        html_path = os.path.join('..', 'templates', "{}.html".format(templatename))
        text_path = os.path.join('..', 'templates', "{}.txt".format(templatename))
        if not check_files(html_path, text_path):
            return 1

        ses = boto3.client('ses')
        with open(html_path) as f:
            html_contents = f.read()

        with open(text_path) as f:
            text_contents = f.read()

        response = ses.update_template(
            Template = {
                'TemplateName' : templatename,
                'SubjectPart'  : 'Welcome to the club',
                'TextPart'     : text_contents,
                'HtmlPart'     : html_contents
            }
        )

        print(response)

@ManageTemplates.subcommand("add")
class AddTemplate(cli.Application):
    DESCRIPTION = "add a new template on aws"
    def main(self, templatename):
        html_path = os.path.join('..', 'templates', "{}.html".format(templatename))
        text_path = os.path.join('..', 'templates', "{}.txt".format(templatename))
        if not check_files(html_path, text_path):
            return 1

        ses = boto3.client('ses')
        with open(html_path) as f:
            html_contents = f.read()

        with open(text_path) as f:
            text_contents = f.read()

        response = ses.create_template(
            Template = {
                'TemplateName' : templatename,
                'SubjectPart'  : 'Welcome to the club',
                'TextPart'     : text_contents,
                'HtmlPart'     : html_contents
            }
        )
            
        print(response)


def check_files(html_path: str, text_path: str) -> bool:
    if os.path.isfile(text_path) and os.path.isfile(html_path):
        return True
    if not os.path.isfile(html_path):
            print("\n\nthe path specified does not exist:", html_path)
    if not os.path.isfile(text_path):
            print("\n\nthe path specified does not exist:", text_path)
    return False


if __name__== "__main__":
    ManageTemplates.run()
