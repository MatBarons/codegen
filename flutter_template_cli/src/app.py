from InquirerPy import inquirer

from create_project.create_flutter_template import create_flutter_project
from custom_widgets.generate_custom_widget import generate_custom_widget


def init_program():
    option = inquirer.select(
        message="What do you want to do:",
        choices=["Generate Flutter project", "Generate custom widget"]
    ).execute()

    if option == "Generate Flutter project":
        create_flutter_project()
    if option == "Generate custom widget":
        generate_custom_widget()

