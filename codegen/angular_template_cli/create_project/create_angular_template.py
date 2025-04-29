from os import listdir, path,getcwd
from subprocess import run
from re import search
from shutil import copy2
from json import load,dump
from codegen.utils.config import Config
from codegen.utils.utils import copy_folders,create_folders,get_angular_data,write_file
from codegen.utils.prompter import question,choose

def add_packages_to_package_json(packages):

    project_path = Config().get("project_path")
    package_json_path = path.join(project_path, "package.json")

    with open(package_json_path, "r") as file:
        data: dict = load(file)

    for package in packages:
        data.setdefault("dependencies", {})[package] = ""
    
    with open(package_json_path, "w") as file:
        dump(data, file, indent=2)
    return


def generate_sass():
    project_path = Config().get("project_path")
    source_dir = path.join(get_angular_data(),"create","sass")
    destination_dir = path.join(project_path,"src","sass")
    copy_folders(source_dir,destination_dir,["styles.scss"])
    return

def generate_global_state():
    project_path = Config().get("project_path")
    source_dir = path.join(get_angular_data(),"create","app-state")
    destination_dir = path.join(project_path,"src","app","app-state")
    copy_folders(source_dir,destination_dir)
    return

def generate_core_module():
    project_path = Config().get("project_path")
    source_dir = path.join(get_angular_data(),"create","core")
    destination_dir = path.join(project_path,"src","app","core")
    copy_folders(source_dir,destination_dir)
    return

def generate_shared_folder():
    project_path = Config().get("project_path")
    source_dir = path.join(get_angular_data(),"create","shared")
    destination_dir = path.join(project_path,"src","app","shared")
    copy_folders(source_dir,destination_dir)
    return

def change_appconfig(project_name):
    project_path = Config().get("project_path")
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

def add_i18n_support(languages):
    project_path = Config().get("project_path")
    add_packages_to_package_json(["@ngneat/transloco"])
    source_dir = path.join(get_angular_data(),"create","i18n")
    destination_dir = path.join(project_path,"src","assets","i18n")
    excluded = []
    #Looking for each language files available in create/i18n and excluding those that weren't requested by the user
    for item in listdir(source_dir):
        item_path = path.join(source_dir, item)
        if (
            path.isfile(item_path)
            and item.endswith(".json")
            and len(item.split(".")) == 2
        ):
            lang_code = item.split(".")[0]
            if lang_code not in [*languages,"it","en"]:
                excluded.append(item)
    copy_folders(source_dir,destination_dir,excluded)
    return 


def create_angular_template():
    project_name = input("Enter the project name: ")
    print(f"Creating Angular project: {project_name}")
    run(["ng", "new", project_name ,"--skip-install"],shell=True,check=True)
    project_path = path.join(getcwd(), project_name)
    Config().set("project_path",project_path)
    generate_sass()
    generate_global_state()
    generate_core_module()
    generate_shared_folder()
    change_appconfig(project_name)
    create_folders(["features"],path.join(project_path,"src","app"))
    add_packages_to_package_json(["@ngrx/effects","@ngrx/router-store","@ngrx/store","@ngrx/store-devtools"])

    languages: str = question("Enter the language codes (e.g. es, fr) separated by commas you wish to add: (en and it are automatically supported)")
    add_i18n_support(languages.split(','))

    design_system = choose("Choose a design library:",["material", "bootstrap", "none"],False)
    core_dir = path.join(project_path,"src","app","core")
    print(f"Adding {design_system} to package.json and pre-built components to core directory")
    copy_folders(path.join(get_angular_data(),"components",design_system,"error"),core_dir)
    copy_folders(path.join(get_angular_data(),"components",design_system,"loader"),core_dir)
    copy_folders(path.join(get_angular_data(),"components",design_system,"snackbars"),core_dir)
    match design_system:
        case "material":
            add_packages_to_package_json(["@angular/material"])
            styles_source_dir = path.join(get_angular_data(),"create","sass","styles.scss")
            styles_destination_dir = path.join(project_path,"src")
            copy2(styles_source_dir,styles_destination_dir)
        case "bootstrap":
            add_packages_to_package_json(["bootstrap"])
 
    print(f"Project creation completed")
            
            
        