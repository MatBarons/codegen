from InquirerPy import inquirer
from .create_project.create_angular_template import create_angular_template
from .custom_widgets.create_custom_widget import create_custom_widget
def init_angular():
    option = inquirer.select(
        message="What you want to do?",
        choices=["Generate new project", "Generate custom component"]
    ).execute()

    if option == "Generate new project":
        create_angular_template()
    if option == "Generate custom component":
        create_custom_widget()
    