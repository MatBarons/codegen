from os import path,walk,makedirs
from re import fullmatch
from codegen.utils.config import Config
from codegen.utils.utils import copy_folders,get_angular_data
from codegen.utils.prompter import confirm,choose,question,browse_dirs

def get_relative_path(target_path, base_path):
    """
    Compute the relative path from one file (base) to another (target).

    Args:
        target_path (str): The destination file path.
        base_path (str): The starting point file path.

    Returns:
        str: Relative path from base_path to target_path.
    """
    return path.relpath(target_path, start=path.dirname(path.abspath(base_path)))

def locate_file_in_project(filename):
    project_path = Config().get("project_root")
    for root, _, files in walk(project_path):
        if filename in files:
            return path.abspath(path.join(root, filename))
    return None

def is_typescript_type(type_str: str) -> bool:
    type_str = type_str.strip()

    # Common TypeScript primitive types
    ts_primitives = {
        "string", "number", "boolean", "null", "undefined",
        "any", "void", "never", "unknown", "object", "bigint", "symbol"
    }

    # Check if it's a simple primitive type
    if type_str in ts_primitives:
        return True

    # Match array types like `string[]` or `Array<number>`
    if fullmatch(r'\w+\[\]', type_str) or fullmatch(r'Array<.+>', type_str):
        return True

    # Match union types like `string | number`
    if fullmatch(r'[\w\s|]+', type_str) and '|' in type_str:
        return True

    # Match tuple types like `[string, number]`
    if fullmatch(r'\[\s*[\w\s,]+\s*\]', type_str):
        return True

    # Match object types like `{ name: string; age: number }`
    if fullmatch(r'\{\s*[^}]+\s*\}', type_str):
        return True

    # Match generics like `Promise<string>` or `Map<string, number>`
    if fullmatch(r'\w+<.+>', type_str):
        return True

    # Match function types like `(x: number) => string`
    if fullmatch(r'\(.+\)\s*=>\s*\w+', type_str):
        return True

    # If none matched, assume it's not a valid TS type
    return False

def add_imports(filename:str,file_to_import:str):
    filepath = path.join(Config().get("models_path"),filename)
    imports = f"imports {filename} from {get_relative_path(file_to_import,filepath)}"
    with open(f"{filepath}.model.ts", "r") as file:
        content = file.read()
    content = imports + content
    with open(f"{filepath}.model.ts", "w") as file:
        content = file.write(content)

def create_interface(filename:str,data_structure: dict):
    models_path = Config().get("models_path")
    filepath = f"{path.join(models_path,filename)}.model.ts"
    with open(filepath, "w") as file:
        file.write(f"export interface {filename}")
        file.write("{")
        for key,value in data_structure:
            file.write(f"{key}:{value}")
        file.write("}")
    return filepath

def create_enum(filename: str, data_structure: list):
    models_path = Config().get("models_path")
    filepath=f"{path.join(models_path,filename)}.model.ts"
    with open(filepath, "w") as file:
        file.write(f"export enum {filename}")
        file.write("{")
        for index,key in enumerate(data_structure):
            file.write(f"{key}={index}")
        file.write("}")
        pass
    return filepath

def parse_data_structure(filename,data_structure_answer: str):
    data_structure = dict()
    for data in data_structure_answer.split(','):
        d = data.split(':')
        data_structure[d[0]] = d[1]
        if not is_typescript_type(d[1]):
            answer : str = choose(f"Is {d[1]} an enum or a new data structure", ["enum","new structure"], False)
            if answer is "enum":
                new_data_structure_answer: str = question(message=f"Please define the {d[1]} enum this way -> value1,value2,value3 (the values of the enum will be an incrementing integer starting from 0)")
                new_enum = create_enum(d[1],new_data_structure_answer.split(","))
                add_imports(filename,new_enum)
            if answer is "new structure":
                new_data_structure_answer: str = question(message=f"Please define the {d[1]} type the same way you wrote the previous data structure -> name:type (eg. email:string,name:string,age:number)")
                new_interface = parse_data_structure(d[1],new_data_structure_answer)
                add_imports(filename,new_interface) 
    return create_interface(filename,data_structure)

def add_filters(data_structure: dict,filename:str):
    with_filters = confirm("Would you like filters?")
    
    if with_filters:
        #TODO: add filters on top of the table and NgRx 
        filter_selections:list = choose("Select which columns will be filtered:",data_structure.keys(),True)
        create_interface(filename,data_structure.fromkeys(filter_selections))
        #TODO: modify componentName.component.ts by adding the filter

def editable_table(data_structure: dict):
    is_table_editable = confirm("Is the table editable?")
    
    if is_table_editable: 
        #TODO: use the table wrapped in a form
        column_selections: list = choose("Select which columns are editable:",data_structure.keys(),True)
        create_interface(data_structure.fromkeys(column_selections))

def generate_table(design_system):
    
    component_path = Config().get("component_path")
    component_name = Config().get("component_name")
    source_dir = path.join(get_angular_data(),"component",design_system,"table")
    copy_folders(source_dir,component_path)

    data_structure_answer: str = question('Write the data structure for the table with the following format -> name:type (eg. email:string,name:string,age:number)')

    models_path = browse_dirs("In which folders the interface should be created? All the following data structures for the filters will be also created there")
    print(models_path)
    Config().set("models_path",models_path)
    data_structure = parse_data_structure(component_name,data_structure_answer)
    
    add_filters(data_structure,f"{component_name}Filters")
    editable_table(data_structure)