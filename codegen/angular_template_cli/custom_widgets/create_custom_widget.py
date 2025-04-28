from os import path,getcwd
from json import load
from codegen.utils.prompter import choose,directory,question
from .generate_table import generate_table
from .generate_breadcrumbs import generate_breadcrumbs

def detect_angular_material_bootstrap():
    with open(path.join(getcwd(),"src","app","package.json"), "r") as file:
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
        component_path = directory("Choose the path where the component will be created")
        component_name = question(message="What's the name of the component?")
        generate_table(component_name,component_path,design_system)
    if option == "Breadcrumbs":
        print(f"Breadcrumbs will be generated in the core directory")
        generate_breadcrumbs()