from codegen.utils.prompter import choose
from .create_project.create_angular_template import create_angular_template
from .custom_widgets.create_custom_widget import create_custom_widget
def init_angular():
    option = choose("What you want to do?",["Generate new project", "Generate custom component"],False)

    if option == "Generate new project":
        create_angular_template()
    if option == "Generate custom component":
        create_custom_widget()
    