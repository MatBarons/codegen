import os
from inquirer import Confirm,Text,Checkbox,Path,prompt
from utils.utils import copy_folders,create_folders,get_angular_data

def add_filters(names: list,component_directory):
    with_filters = prompt(Confirm(
            name='table-filters',
            message="Would you like filters?", default=False
        ))
    
    if with_filters:
        #TODO: add filters on top of the table and NgRx 
        filter_selections = prompt(Checkbox(
            name='filters-columns',
            message="Select which columns will be filtered:",
            choices=names.append('None')
        ))

def editable_table(names: list,component_directory):
    is_table_editable = prompt(Confirm(
        name='table-editable',
        message="Is the table editable?", default=False
    ))
    
    if is_table_editable: 
        #TODO: use the table wrapped in a form
        column_selections: list = prompt(Checkbox(
            name='editable-columns',
            message="Select which columns are editable:",
            choices=names.append('None')
        ))  

def generate_table(component_name,component_directory,design_system):
    
    source_dir = os.path.join(get_angular_data(),"component",design_system,"table")
    destination_dir = os.path.join(component_directory)
    copy_folders(source_dir,destination_dir)

    data_structure: str = prompt(Text(
        name='data-structure',
        message='Write the data structure for the table with the following format -> name:type (eg. email:string,name:string,age:number)'
    ))

    models_path = prompt(Path(
        name='component_path',
        message="In which folders the interface should be created? All the following data structures for the filters will be also created there",
        path_type=Path.DIRECTORY
    ))

    with open(f"{models_path}/{component_name}.model.ts", "w") as file:
        file.write(f"export interface {component_name} {{ \n {data_structure.replace(',',',\n')} }}")
        pass 
 
    names = [pair.split(":")[0] for pair in data_structure.split(",")]
    add_filters(names,component_directory)
    editable_table(names,component_directory)