from os import path
from re import search

from codegen.utils.config import Config
from .pubspec import modify_pubspec_yaml
from codegen.utils.utils import copy_folders,write_file,get_flutter_data


def add_sqlflite_support():
    project_path = Config().get("project_path")
    main_dart_path = path.join(project_path, "lib", "main.dart")
    modify_pubspec_yaml(project_path, "sqflite")
    modify_pubspec_yaml(project_path, "path")
    add_files(project_path) 
    add_sqlflite_to_main(main_dart_path)

def add_files():
    project_path = Config().get("project_path")
    providers_source_dir = path.join(get_flutter_data(),"create","sqlflite")
    providers_destination_dir = path.join(project_path, "lib", "providers","sqlflite")
    copy_folders(providers_source_dir,providers_destination_dir)

def add_sqlflite_to_main():
    project_path = Config().get("project_path")
    main_dart_path = path.join(project_path, "lib", "main.dart")
    with open(main_dart_path, "r") as file:
        content = file.read()

    sqlflite_imports = """
import 'providers/sqlflite/database_helper.dart';    
"""


    sql_lite_main = """
    DatabaseHelper dbHelper = DatabaseHelper.instance;
"""

    main_function_pattern = r"void\s+main\s*\(\s*\)\s+async\s*\{"
    main_function_match = search(main_function_pattern,content)
    content = write_file(main_function_match,sql_lite_main,content)

    if sqlflite_imports.strip() not in content:
        content = sqlflite_imports.strip() + content
    with open(main_dart_path, "w") as file:
        file.write(content)