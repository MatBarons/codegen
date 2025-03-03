from InquirerPy import inquirer

def generate_custom_widget():
    option = inquirer.select(
        message="What do you want to do:",
        choices=["Generate table", "Generate navigation bar"]
    ).execute()

    if option == "Generate table":
        print('qui')

    if option == "Generate navigation bar":
        print('qui')
