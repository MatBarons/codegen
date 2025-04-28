from codegen.utils.prompter import choose

def create_custom_widget():
    option = choose("What do you want to do:",["Generate table", "Generate navigation bar"],False)

    if option == "Generate table":
        print('qui')

    if option == "Generate navigation bar":
        print('qui')
