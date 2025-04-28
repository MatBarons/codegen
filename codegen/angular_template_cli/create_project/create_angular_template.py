from os import path,getcwd
from subprocess import run
from shutil import copy2
from codegen.utils.utils import copy_folders,create_folders,get_angular_data
from codegen.utils.prompter import question,choose

def generate_sass(project_path):
    source_dir = path.join(get_angular_data(),"create","sass")
    destination_dir = path.join(project_path,"src")
    copy_folders(source_dir,path.join(destination_dir,"sass"))
    return

def generate_global_state(project_path):
    source_dir = path.join(get_angular_data(),"create","app-state")
    destination_dir = path.join(project_path,"src","app")
    copy_folders(source_dir,path.join(destination_dir,"app-state"))
    return

def generate_core_module(project_path):
    source_dir = path.join(get_angular_data(),"create","core")
    destination_dir = path.join(project_path,"src","app")
    copy_folders(source_dir,path.join(destination_dir,"core"))
    return

def generate_shared_folder(project_path):
    source_dir = path.join(get_angular_data(),"create","shared")
    destination_dir = path.join(project_path,"src","app")
    copy_folders(source_dir,path.join(destination_dir,"shared"))
    return

def change_appconfig(project_path):
    source_file = path.join(get_angular_data(),"create","appconfig.ts")
    destination_dir = path.join(project_path,"src","app")
    copy2(source_file,destination_dir)
    return

def add_i18n_support(project_path, languages):
    source_dir = path.join(get_angular_data(),"create","i18n")
    destination_dir = path.join(project_path,"src","assets")
    copy_folders(source_dir,path.join(destination_dir,"i18n"))
    return 

def create_angular_template():
    project_name = question("Enter the project name: ")
    print(f"Creating Angular project: {project_name}")
    run(["ng", "new", project_name],shell=True,check=True)
    
    project_path = path.join(getcwd(), project_name)
    generate_sass(project_path)
    generate_global_state(project_path)
    generate_core_module(project_path)
    generate_shared_folder(project_path)
    change_appconfig(project_path)
    create_folders(["features"],path.join(project_path,"src","app"))

    add_i18n = question("Would you like to add i18n support?")

    if add_i18n:
        languages: str = question("Enter the language codes (e.g. es, fr) separated by commas: (en and it are automatically supported)")
        add_i18n_support(project_path, languages.split(','))

    design_system = choose("Choose a design library:",["material", "bootstrap", "none"],False)
    core_dir = path.join(project_path,"src","app","core")
    copy_folders(path.join(get_angular_data(),"components",design_system,"error"),core_dir)
    copy_folders(path.join(get_angular_data(),"components",design_system,"loader"),core_dir)
    copy_folders(path.join(get_angular_data(),"components",design_system,"snackbars"),core_dir)
    match design_system:
        case "material":
            run(["npm", "install", "@angular/material"],shell=True,check=True,cwd=project_path) 
        case "bootstrap":
            run(["npm", "install", "bootstrap"],shell=True,check=True,cwd=project_path)
            
            
        