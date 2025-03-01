from InquirerPy import inquirer

from src.flutter_template_cli.src.app import init_program as init_flutter
from src.angular_template_cli.src.app import init_program as init_angular


def init_program():
    option = inquirer.select(
        message="Which framework are you using:",
        choices=["Flutter", "Angular"]
    ).execute()

    if option == "Flutter":
        init_flutter()
    if option == "Angular":
        init_angular() 


if __name__ == "__main__":
    init_program()