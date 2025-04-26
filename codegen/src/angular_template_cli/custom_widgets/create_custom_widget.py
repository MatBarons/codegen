from os import path,getcwd
from json import load
from inquirer import Text,List,Path,prompt
from .generate_table import generate_table

def detect_angular_material_bootstrap():
    with open(path.join(getcwd(),"src","app","package.json"), "r") as file:
        data: dict = load(file)

    dependencies = data.get("dependencies", {})
    dev_dependencies = data.get("devDependencies", {})
    all_packages = {**dependencies, **dev_dependencies}

    if "@angular/material" in all_packages:
        return "material"
    if "bootstrap" in all_packages:
        return "bootstrap"
    return None


def create_custom_widget():
    option = prompt(List(
        name='components-material',
        message="What custom component you want to create?",
        choices=["Table", "Breadcrumbs"]
    ))

    component_path = prompt(Path(
        name='component_path',
        message="Choose the path where the component will be created",
        path_type=Path.DIRECTORY
    ))

    component_name = prompt(Text(
        name='component_name',
        message="What's the name of the component?",
        path_type=Path.DIRECTORY
    ))

    design_system = detect_angular_material_bootstrap()

    if option == "Table":
        generate_table(component_name,component_path,design_system)

    

    #if option == "Breadcrumbs":
        #generate_breadcrumbs()