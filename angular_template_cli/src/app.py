from InquirerPy import inquirer

from .create_project.create_angular_template import create_angular_template



def init_program():
    option = inquirer.select(
        message="What you want to do:",
        choices=[
            "Generate new Angular project",
            "Generate custom widget"
        ]
    ).execute()

    if option == "Generate new Angular project":
        create_angular_template()



if __name__ == "__main__":
    init_program()