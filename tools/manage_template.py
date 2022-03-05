"""Manages the templates in the aws ses services
    must have templates in the "templates" direct named the same as the template specifed
    for example, if you specified "salted" as the template name, we expect to find:
        salted.html
        salted.txt
    in the "templates" directory
"""
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
    def main(self, templatename: str) -> int:
        """updates the specifed template

        Args:
            templatename (str): the template to update

        Returns:
            int: return code
        """
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
    def main(self, templatename: str) -> int:
        """Adds a new template to AWS ses services

        Args:
            templatename (str): the name of the template to add

        Returns:
            int: retrun code
        """
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
    """checks to see if all the needed files are present in the template directory

    Args:
        html_path (str): path to the *.html file
        text_path (str): path to the *.txt file

    Returns:
        bool: true if the files are all present
    """
    if os.path.isfile(text_path) and os.path.isfile(html_path):
        return True
    if not os.path.isfile(html_path):
            print("\n\nthe path specified does not exist:", html_path)
    if not os.path.isfile(text_path):
            print("\n\nthe path specified does not exist:", text_path)
    return False


if __name__== "__main__":
    ManageTemplates.run()
