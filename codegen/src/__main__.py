from InquirerPy import inquirer
from .angular_template_cli.init_angular import init_angular
from .flutter_template_cli.init_flutter import init_flutter

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