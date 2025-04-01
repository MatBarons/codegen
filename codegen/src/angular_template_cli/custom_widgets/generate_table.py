from inquirer import Confirm,Text,prompt

def table_add_ons():
    with_filters = prompt(Confirm(
            name='table-filters',
            message="Would you like filters?", default=False
        ))
    is_table_editable= prompt(Confirm(
        name='table-editable',
        message="Is the table editable?", default=False
    ))
    if is_table_editable: 

def generate_table():
    data_structure = prompt(Text(
        name='data-structure',
        message='Write the data structure for the table with the following format -> name:type (eg. email:string)'
    ))
    data_structure
    table_add_ons()