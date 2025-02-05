from InquirerPy import inquirer



def init_program():
    option = inquirer.select(
        message="Which component you want to create:",
        choices=[
            "Generate table",
            "Generate custom widget"
        ]
    ).execute()



if __name__ == "__main__":
    init_program()