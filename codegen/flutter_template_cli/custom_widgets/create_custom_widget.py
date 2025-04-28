from inquirer import List,prompt

def create_custom_widget():
    option = prompt(List(
        name='flutter-widgets',
        message="What do you want to do:",
        choices=["Generate table", "Generate navigation bar"]
    ))

    if option == "Generate table":
        print('qui')

    if option == "Generate navigation bar":
        print('qui')
