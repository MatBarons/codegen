from os import path,makedirs,listdir,getcwd, walk
from shutil import copytree,copy2,ignore_patterns
import sys
from codegen.utils.config import Config

def create_gitkeep(folder_path):
    gitkeep_path = path.join(folder_path, ".gitkeep")
    with open(gitkeep_path, "w") as file:
        pass 

def create_folders(folders_to_create,path_to_create):
    for folder in folders_to_create:
        folder_path = path.join(path_to_create, folder)
        makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        create_gitkeep(folder_path)

def copy_folders(source_dir,destination_dir,exclude=None):
    if exclude is None:
        exclude = []

    source_dir = path.abspath(source_dir)
    destination_dir = path.abspath(destination_dir)

    folder_name = path.basename(source_dir)

    # Avoid duplicating the folder if destination already ends with it
    if not path.basename(destination_dir) == folder_name:
        target_path = path.join(destination_dir, folder_name)
    else:
        target_path = destination_dir

    # Prevent self-copy
    if path.normpath(source_dir) == path.normpath(target_path):
        print(f"Skipping: source and destination are the same: {source_dir}")
        return

    if not path.exists(target_path):
        copytree(
            source_dir,
            target_path,
            ignore=ignore_patterns(*exclude)
        )
    else:
        for item in listdir(source_dir):
            if item in exclude:
                continue

            s_item = path.join(source_dir, item)
            d_item = path.join(target_path, item)

            if path.isdir(s_item):
                copy_folders(s_item, target_path, exclude)
            else:
                makedirs(target_path, exist_ok=True)
                copy2(s_item, d_item)

def write_file(match,content_to_copy,content):
    if not match:
        print("Could not find {match}")
        return 
    
    insert_position_main = match.end()
    return content[:insert_position_main] + content_to_copy + content[insert_position_main:]


def get_relative_path(target_path, base_path):
    """
    Compute the relative path from one file (base) to another (target).

    Args:
        target_path (str): The destination file path.
        base_path (str): The starting point file path.

    Returns:
        str: Relative path from base_path to target_path.
    """
    return path.relpath(target_path, start=path.dirname(path.abspath(base_path)))

def locate_file_in_project(filename):
    project_path = Config().get("project_root")
    for root, _, files in walk(project_path):
        if filename in files:
            return path.abspath(path.join(root, filename))
    return None

def get_base_path():
    if getattr(sys, 'frozen', False):
        # Running from bundled executable
        return sys._MEIPASS
    else:
        # Running from source
        cwd = getcwd()
        if "codegen" in path.basename(path.normpath(cwd)).lower():
            return cwd
        else:
            while True:
                cwd = path.dirname(cwd)
                if "codegen" in path.basename(path.normpath(cwd)).lower():
                    return cwd



def get_angular_data():
    return path.join(get_base_path(),"data","angular")

def get_flutter_data():
    return path.join(get_base_path(),"data","flutter")