import os
import subprocess
from InquirerPy import inquirer

from .i18n import add_i18n_support

def run_ng_new(project_name):
    print(f"Creating Flutter project: {project_name}")
    subprocess.run(["ng", "new", project_name],shell=True,check=True)

def create_angular_template():
    project_name = input("Enter the project name: ")
    run_ng_new(project_name)
    
    project_path = os.path.join(os.getcwd(), project_name)

    add_i18n = inquirer.confirm(
        message="Would you like to add i18n support?", default=False
    ).execute()

    if add_i18n:
        languages = inquirer.text(
            message="Enter the language codes (e.g. es, fr) separated by commas: (en and it are automatically supported)",
            validate=lambda result: len(result) > 0
        ).execute().split(',')
        add_i18n_support(project_path, languages)
        