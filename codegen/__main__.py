from inquirer import List,prompt
from .angular_template_cli.init_angular import init_angular
from .flutter_template_cli.init_flutter import init_flutter

def init_program():
    option = prompt(List(
        name='init-project',
        message="Which framework are you using:",
        choices=["Flutter", "Angular"]
    ))

    if option == "Flutter":
        init_flutter()
    if option == "Angular":
        init_angular() 


if __name__ == "__main__":
    init_program()