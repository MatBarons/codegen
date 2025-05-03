from os import path,getcwd
from json import load
from codegen.utils.config import Config
from codegen.utils.prompter import choose,browse_dirs,question
from .generate_table import generate_table
from .generate_breadcrumbs import generate_breadcrumbs

def detect_angular_material_bootstrap():
    with open(path.join(getcwd(),"package.json"), "r") as file:
        data: dict = load(file)

    all_packages = {**data.get("dependencies", {}), **data.get("devDependencies", {})}

    if "@angular/material" in all_packages:
        return "material"
    if "bootstrap" in all_packages:
        return "bootstrap"
    return None


def create_custom_widget():
    option = choose("What custom component you want to create?",["Table", "Breadcrumbs"],False)
    design_system = detect_angular_material_bootstrap()

    if option == "Table":
        component_path = browse_dirs("Choose the path where the component will be created")
        Config().set("component_path",component_path)
        print(component_path)
        component_name = question("What's the name of the component?")
        Config().set("component_name",component_name)
        print(component_name)
        generate_table(design_system)
    if option == "Breadcrumbs":
        print(f"Breadcrumbs will be generated in the core directory")
        generate_breadcrumbs()