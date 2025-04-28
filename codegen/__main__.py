from .angular_template_cli.init_angular import init_angular
from .flutter_template_cli.init_flutter import init_flutter
from codegen.utils.prompter import choose

def init_program():
    option = choose("Which framework are you using:",["Flutter", "Angular"],False)
    print(option)
    if option == "Flutter":
        init_flutter()
    if option == "Angular":
        init_angular() 


if __name__ == "__main__":
    init_program()