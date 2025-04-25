import subprocess
from inquirer import List,Path,prompt
from .generate_table import generate_table

def detect_angular_material_bootstrap():
    return
    #with open(os.path.join(os.getcwd(),"src","app","package.json"), "r") as file:
        
        

def create_custom_widget():
    option = prompt(List(
        name='components-material',
        message="What custom component you want to create?",
        choices=["Table", "Breadcrumbs"]
    ))

    design_system = detect_angular_material_bootstrap()

    if option == "Table":
        generate_table()

    component_path = prompt(Path(
        name='component_path',
        message="Choose the path where the component will be created",
        path_type=Path.DIRECTORY
    ))
    subprocess.run(["ng","g","c",""],cwd=component_path)

    #if option == "Breadcrumbs":
        #generate_breadcrumbs()