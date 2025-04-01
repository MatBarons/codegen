from inquirer import List
from .create_project.create_flutter_template import create_flutter_template
from .custom_widgets.create_custom_widget import create_custom_widget
def init_flutter():
    option = List(
        name='init-flutter',
        message="What you want to do?",
        choices=["Generate new project", "Generate custom component"]
    ).execute()

    if option == "Generate new project":
        create_flutter_template()
    if option == "Generate custom component":
        create_custom_widget()