import subprocess
import os
from codegen.utils.config import Config
from codegen.utils.prompter import choose,confirm,question
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
    Config().set("project_path",project_path)
    # Add folders
    folders = [
            "lib/services",
            "lib/widgets",
            "lib/screens",
            "lib/models",
            "lib/utils"
        ]
    create_folders(folders,project_path)
    setup_main()

    add_http_interceptor = confirm("Would you like to add HTTP interceptor support?")

    if add_http_interceptor:
        add_http_interceptor_support()

    # Step 2: Ask if Redux should be added
    add_redux = confirm("Would you like to add Redux support?")

    if add_redux:
        add_redux_support(add_http_interceptor)

    # Step 3: Ask if l10n should be added
    add_l10n = confirm("Would you like to add localization (l10n) support?")

    if add_l10n:
        languages: str = question("Enter the language codes (e.g. en, es, fr) separated by commas: (en and it are automatically supported)")
        add_l10n_support(languages.split(','))

    # Step 4: Ask if sqlite (sqflite) should be added
    add_sqlite = confirm("Would you like to add SQLite support (sqflite package)?")

    if add_sqlite:
        add_sqlflite_support()

    # Step 5: Ask for login type
    login_type = choose("Choose a login method:",["keycloak", "azure", "cognito", "magic", "none"],False)

    #if login_type != "none":
        #add_login_support(login_type)

    print(f"Flutter project {project_name} created and configured successfully.")
