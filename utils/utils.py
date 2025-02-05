import os


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