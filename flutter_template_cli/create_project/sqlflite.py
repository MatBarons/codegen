import os
import re
import shutil
from .pubspec import modify_pubspec_yaml
from utils.utils import copy_folders,write_file


def add_sqlflite_support(project_path,main_dart_path):
    modify_pubspec_yaml(project_path, "sqflite")
    modify_pubspec_yaml(project_path, "path")
    add_files(project_path) 
    add_sqlflite_to_main(main_dart_path)


def add_files(project_path):
    providers_source_dir = os.path.join(os.getcwd(), "src","create_project","data","sqlflite")
    providers_destination_dir = os.path.join(project_path, "lib", "providers","sqlflite")
    copy_folders(providers_source_dir,providers_destination_dir)

def add_sqlflite_to_main(main_dart_path):
    with open(main_dart_path, "r") as file:
        content = file.read()

    sqlflite_imports = """
import 'providers/sqlflite/database_helper.dart';    
"""


    sql_lite_main = """
    DatabaseHelper dbHelper = DatabaseHelper.instance;
"""

    main_function_pattern = r"void\s+main\s*\(\s*\)\s+async\s*\{"
    main_function_match = re.search(main_function_pattern,content)
    write_file(main_function_match,sql_lite_main)

    if sqlflite_imports.strip() not in content:
        content = sqlflite_imports.strip() + content
    with open(main_dart_path, "w") as file:
        file.write(content)