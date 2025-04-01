from inquirer import Confirm,List

def detect_angular_bootstrap():
    

def table_add_ons():
    with_filters = Confirm(
            name='table-filters',
            message="Would you like filters?", default=False
        )
    is_table_editable= Confirm(
        name='table-editable',
        message="Is the table editable?", default=False
    )
    if is_table_editable: 

def create_custom_widget():
    option = List(
        name='components-material',
        message="What custom component you want to create?",
        choices=["Table", "Breadcrumbs",""]
    )

    detect_angular_bootstrap()

    if option == "Table":
        table_add_ons()


        
    if option == "Breadcrumbs":
        