from inquirer import Confirm,Text,Checkbox,Path,prompt

def table_add_ons(data_structure):
    names = [pair.split(":")[0] for pair in data_structure]

    with_filters = prompt(Confirm(
            name='table-filters',
            message="Would you like filters?", default=False
        ))
    #TODO: add filters on top of the table and NgRx
    if with_filters:
        filter_selections = prompt(Checkbox(
            name='filters-columns',
            message="Select which columns will be filtered:",
            choices=names.append('None')
        ))

    is_table_editable = prompt(Confirm(
        name='table-editable',
        message="Is the table editable?", default=False
    ))
    #TODO: use the table wrapped in a form
    if is_table_editable: 
        column_selections: list = prompt(Checkbox(
            name='editable-columns',
            message="Select which columns are editable:",
            choices=names.append('None')
        ))

def generate_table(component_name):

    #TODO: 

    data_structure: str = prompt(Text(
        name='data-structure',
        message='Write the data structure for the table with the following format -> name:type (eg. email:string,name:string,age:number)'
    ))
    pairs = data_structure.split(",")

    models_path = prompt(Path(
        name='component_path',
        message="In which folders the interface should be created? All the following data structures for the filters will be also created there",
        path_type=Path.DIRECTORY
    ))

    with open(models_path, "w") as file:
        file.write("export interface ")
        pass 
 
    table_add_ons(pairs)