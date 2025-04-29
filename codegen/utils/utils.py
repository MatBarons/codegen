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

def copy_folders(source_dir,destination_dir,exclude=None):
    if exclude is None:
        exclude = []

    source_dir = os.path.abspath(source_dir)
    destination_dir = os.path.abspath(destination_dir)

    folder_name = os.path.basename(source_dir)

    # Avoid duplicating the folder if destination already ends with it
    if not os.path.basename(destination_dir) == folder_name:
        target_path = os.path.join(destination_dir, folder_name)
    else:
        target_path = destination_dir

    # Prevent self-copy
    if os.path.normpath(source_dir) == os.path.normpath(target_path):
        print(f"Skipping: source and destination are the same: {source_dir}")
        return

    if not os.path.exists(target_path):
        shutil.copytree(
            source_dir,
            target_path,
            ignore=shutil.ignore_patterns(*exclude)
        )
    else:
        for item in os.listdir(source_dir):
            if item in exclude:
                continue

            s_item = os.path.join(source_dir, item)
            d_item = os.path.join(target_path, item)

            if os.path.isdir(s_item):
                copy_folders(s_item, target_path, exclude)
            else:
                os.makedirs(target_path, exist_ok=True)
                shutil.copy2(s_item, d_item)

def write_file(match,content_to_copy,content):
    if not match:
        print("Could not find {match}")
        return 
    
    insert_position_main = match.end()
    return content[:insert_position_main] + content_to_copy + content[insert_position_main:]


def get_angular_data():
    return os.path.join(os.getcwd(),"data","angular")

def get_flutter_data():
    return os.path.join(os.getcwd(),"data","flutter")