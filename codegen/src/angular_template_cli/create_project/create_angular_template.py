import os
import subprocess
import shutil
from InquirerPy import inquirer
from utils.utils import copy_folders,create_folders,get_angular_data

def run_ng_new(project_name):
    print(f"Creating Angular project: {project_name}")
    subprocess.run(["ng", "new", project_name],shell=True,check=True)

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
    run_ng_new(project_name)
    
    project_path = os.path.join(os.getcwd(), project_name)
    generate_sass(project_path)
    generate_global_state(project_path)
    generate_core_module(project_path)
    generate_shared_folder(project_path)
    change_appconfig(project_path)
    create_folders(["features"],os.path.join(project_path,"src","app"))

    add_i18n = inquirer.confirm(
        message="Would you like to add i18n support?", default=False
    ).execute()

    if add_i18n:
        languages = inquirer.text(
            message="Enter the language codes (e.g. es, fr) separated by commas: (en and it are automatically supported)",
            validate=lambda result: len(result) > 0
        ).execute().split(',')
        add_i18n_support(project_path, languages)
        