from os import path,getcwd
from subprocess import run
from re import search
from shutil import copy2
from json import load,dump
from codegen.utils.utils import copy_folders,create_folders,get_angular_data,write_file
from codegen.utils.prompter import question,choose,confirm

def generate_sass(project_path):
    source_dir = path.join(get_angular_data(),"create","sass")
    destination_dir = path.join(project_path,"src","sass")
    copy_folders(source_dir,destination_dir,["styles.scss"])
    styles_source_dir = path.join(get_angular_data(),"create","sass","styles.scss")
    styles_destination_dir = path.join(project_path,"src")
    copy2(styles_source_dir,styles_destination_dir)
    return

def generate_global_state(project_path):
    source_dir = path.join(get_angular_data(),"create","app-state")
    destination_dir = path.join(project_path,"src","app","app-state")
    copy_folders(source_dir,destination_dir)
    return

def generate_core_module(project_path):
    source_dir = path.join(get_angular_data(),"create","core")
    destination_dir = path.join(project_path,"src","app","core")
    copy_folders(source_dir,destination_dir)
    return

def generate_shared_folder(project_path):
    source_dir = path.join(get_angular_data(),"create","shared")
    destination_dir = path.join(project_path,"src","app","shared")
    copy_folders(source_dir,destination_dir)
    return

def change_appconfig(project_path,project_name):
    source_file = path.join(get_angular_data(),"create","app.config.ts")
    destination_dir = path.join(project_path,"src","app")
    copy2(source_file,destination_dir)
    with open(path.join(destination_dir,"app.config.ts"),"r") as f:
        content = f.read()
    pattern = r"project_name"
    match = search(pattern,content)
    content = write_file(match,project_name,content)
    content.replace("project_name", '')
    with open(path.join(destination_dir,"app.config.ts"), "w") as file:
        file.write(content)
    return

def add_i18n_support(project_path, languages):
    source_dir = path.join(get_angular_data(),"create","i18n")
    destination_dir = path.join(project_path,"src","assets","i18n")
    copy_folders(source_dir,destination_dir)
    return 

def add_design_system(project_path,design_system):
    package_json_path = path.join(project_path, "package.json")

    with open(package_json_path, "r") as file:
        data: dict = load(file)

    match design_system:
        case "material":
            data.setdefault("dependencies", {})["@angular/material"] = ""
        case "bootstrap":
            data.setdefault("dependencies", {})["bootstrap"] = ""

    with open(package_json_path, "w") as file:
        dump(data, file, indent=2)



def create_angular_template():
    project_name = question("Enter the project name: ")
    print(f"Creating Angular project: {project_name}")
    run(["ng", "new", project_name ,"--skip-install"],shell=True,check=True)
    
    project_path = path.join(getcwd(), project_name)
    generate_sass(project_path)
    generate_global_state(project_path)
    generate_core_module(project_path)
    generate_shared_folder(project_path)
    change_appconfig(project_path,project_name)
    create_folders(["features"],path.join(project_path,"src","app"))

    add_i18n = confirm("Would you like to add i18n support?")
    if add_i18n:
        languages: str = question("Enter the language codes (e.g. es, fr) separated by commas: (en and it are automatically supported)")
        add_i18n_support(project_path, languages.split(','))

    design_system = choose("Choose a design library:",["material", "bootstrap", "none"],False)
    core_dir = path.join(project_path,"src","app","core")
    copy_folders(path.join(get_angular_data(),"components",design_system,"error"),core_dir)
    copy_folders(path.join(get_angular_data(),"components",design_system,"loader"),core_dir)
    copy_folders(path.join(get_angular_data(),"components",design_system,"snackbars"),core_dir)
    print(f"Adding {design_system} to package.json and pre-built components to core directory")
    add_design_system(project_path,design_system)
 
    print(f"Project creation completed")
            
            
        