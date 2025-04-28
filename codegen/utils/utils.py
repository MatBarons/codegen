import os
import shutil

def create_gitkeep(folder_path):
    gitkeep_path = os.path.join(folder_path, ".gitkeep")
    with open(gitkeep_path, "w") as file:
        pass 

def create_folders(folders_to_create,project_path):
    for folder in folders_to_create:
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        create_gitkeep(folder_path)

def copy_folders(source_dir,destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
    
    # Copy each item (file or subfolder) from 'source_dir' to 'destination_dir'
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, destination_item)
    return

def write_file(match,content_to_copy):
    if not match:
        print("Could not find {match}")
        return 
    
    insert_position_main = match.end()
    content = content[:insert_position_main] + content_to_copy + content[insert_position_main:]


def get_angular_data():
    return os.path.join(os.getcwd(),"data","angular")

def get_flutter_data():
    return os.path.join(os.getcwd(),"data","flutter")