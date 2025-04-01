from inquirer import List

def create_custom_widget():
    option = List(
        name='flutter-widgets',
        message="What do you want to do:",
        choices=["Generate table", "Generate navigation bar"]
    )

    if option == "Generate table":
        print('qui')

    if option == "Generate navigation bar":
        print('qui')
