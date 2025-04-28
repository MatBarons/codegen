import subprocess
import os
from inquirer import Text,Confirm,List,prompt

from codegen.utils.utils import create_folders

from .http_interceptor import add_http_interceptor_support
from .l10n import add_l10n_support
from .login import add_login_support
from .redux import add_redux_support
from .setup_main import setup_main
from .sqlflite import add_sqlflite_support

def run_flutter_create(project_name):
    #Creates a new Flutter project using 'flutter create'.
    print(f"Creating Flutter project: {project_name}")
    subprocess.run(["flutter", "create", project_name],shell=True,check=True)

def create_flutter_template():
    # Step 1: Ask for project name and create the project
    project_name = input("Enter the project name: ")
    run_flutter_create(project_name)

    # Define project path for modification
    project_path = os.path.join(os.getcwd(), project_name)
    main_dart_path = os.path.join(project_path, "lib", "main.dart")
    # Add folders
    folders = [
            "lib/services",
            "lib/widgets",
            "lib/screens",
            "lib/models",
            "lib/utils"
        ]
    create_folders(folders,project_path)
    setup_main(main_dart_path)

    add_http_interceptor = prompt(Confirm(
        name='interceptors',
        message="Would you like to add HTTP interceptor support?", default=False
    ))

    if add_http_interceptor:
        add_http_interceptor_support(project_path)

    # Step 2: Ask if Redux should be added
    add_redux = prompt(Confirm(
        name='Redux',
        message="Would you like to add Redux support?", default=False
    ))

    if add_redux:
        add_redux_support(project_path,main_dart_path,add_http_interceptor)

    # Step 3: Ask if l10n should be added
    add_l10n = prompt(Confirm(
        name='l10n',
        message="Would you like to add localization (l10n) support?", default=False
    ))

    if add_l10n:
        languages: str = prompt(Text(
            name='languages',
            message="Enter the language codes (e.g. en, es, fr) separated by commas: (en and it are automatically supported)"
        ))
        add_l10n_support(project_path, languages.split(','),main_dart_path)

    # Step 4: Ask if sqlite (sqflite) should be added
    add_sqlite = prompt(Confirm(
        name='sqlite',
        message="Would you like to add SQLite support (sqflite package)?", default=False
    ))

    if add_sqlite:
        add_sqlflite_support(project_path,main_dart_path)

    # Step 5: Ask for login type
    login_type = prompt(List(
        name='login-type',
        message="Choose a login method:",
        choices=["keycloak", "azure", "cognito", "magic", "none"],
    ))

    #if login_type != "none":
        #add_login_support(project_path, login_type,main_dart_path)

    print(f"Flutter project {project_name} created and configured successfully.")
