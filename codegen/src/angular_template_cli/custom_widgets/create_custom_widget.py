from InquirerPy import inquirer

def create_custom_widget():
    option = inquirer.select(
        message="What custom component you want to create?",
        choices=["Table", "Generate custom component"]
    ).execute()

    if option == "Table":
        
    if option == "Generate custom component":
        