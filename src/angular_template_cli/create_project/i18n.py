import os
from utils.utils import copy_folders


def add_i18n_support(project_path, languages):
    source_dir = os.path.join(os.getcwd(),"create_project","data","i18n")
    destination_dir = os.path.join(project_path,"src","assets")
    copy_folders(source_dir,destination_dir)
    return 