from inquirer import Confirm,List,prompt
from .generate_table import generate_table

def detect_angular_material_bootstrap():

def create_custom_widget():
    option = prompt(List(
        name='components-material',
        message="What custom component you want to create?",
        choices=["Table", "Breadcrumbs",""]
    ))

    if option == "Table":
        generate_table()

    if option == "Breadcrumbs":