import os
import subprocess
import shutil
from inquirer import Confirm,List,Text,prompt
from utils.utils import copy_folders,create_folders,get_angular_data

def generate_sass(project_path):
    source_dir = os.path.join(get_angular_data(),"create","sass")
    destination_dir = os.path.join(project_path,"src")
    copy_folders(source_dir,destination_dir)
    return

def generate_global_state(project_path):
    source_dir = os.path.join(get_angular_data(),"create","app-state")
    destination_dir = os.path.join(project_path,"src","app")
    copy_folders(source_dir,destination_dir)
    return

def generate_core_module(project_path):
    source_dir = os.path.join(get_angular_data(),"create","core")
    destination_dir = os.path.join(project_path,"src","app")
    copy_folders(source_dir,destination_dir)
    return

def generate_shared_folder(project_path):
    source_dir = os.path.join(get_angular_data(),"create","shared")
    destination_dir = os.path.join(project_path,"src","app")
    copy_folders(source_dir,destination_dir)
    return

def change_appconfig(project_path):
    source_file = os.path.join(get_angular_data(),"create","appconfig.ts")
    destination_dir = os.path.join(project_path,"src","app")
    shutil.move(source_file,destination_dir)
    return

def add_i18n_support(project_path, languages):
    source_dir = os.path.join(get_angular_data(),"create","i18n")
    destination_dir = os.path.join(project_path,"src","assets")
    copy_folders(source_dir,destination_dir)
    return 

def create_angular_template():
    project_name = input("Enter the project name: ")
    print(f"Creating Angular project: {project_name}")
    subprocess.run(["ng", "new", project_name],shell=True,check=True)
    
    project_path = os.path.join(os.getcwd(), project_name)
    generate_sass(project_path)
    generate_global_state(project_path)
    generate_core_module(project_path)
    generate_shared_folder(project_path)
    change_appconfig(project_path)
    create_folders(["features"],os.path.join(project_path,"src","app"))

    add_i18n = prompt(Confirm(
        name='i18n-confirm',
        message="Would you like to add i18n support?", default=False
    ))

    if add_i18n:
        languages: str = prompt(Text(
            name='i18n-text',
            message="Enter the language codes (e.g. es, fr) separated by commas: (en and it are automatically supported)"
        ))
        add_i18n_support(project_path, languages.split(','))

    design_system = prompt(List(
        name='design',
        message="Choose a design library:",
        choices=["material", "bootstrap", "none"]
    ))
    
    match design_system:
        case "material":
            subprocess.run(["npm", "install", "@angular/material"],shell=True,check=True,cwd=project_path)
            core_dir = os.path.join(project_path,"src","app","core")
            copy_folders(os.path.join(get_angular_data(),"components","material","error"),core_dir)
            copy_folders(os.path.join(get_angular_data(),"components","material","loader"),core_dir)
            copy_folders(os.path.join(get_angular_data(),"components","material","snackbar"),core_dir)
        case "bootstrap":
            subprocess.run(["npm", "install", "bootstrap"],shell=True,check=True,cwd=project_path)
            core_dir = os.path.join(project_path,"src","app","core")
            copy_folders(os.path.join(get_angular_data(),"components","bootstrap","error"),core_dir)
            copy_folders(os.path.join(get_angular_data(),"components","bootstrap","loader"),core_dir)
            copy_folders(os.path.join(get_angular_data(),"components","bootstrap","snackbar"),core_dir)
            
            
        