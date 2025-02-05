import os
import re
import shutil
from .pubspec import modify_pubspec_yaml


def add_sqlflite_support(project_path,main_dart_path):
    modify_pubspec_yaml(project_path, "sqflite")
    modify_pubspec_yaml(project_path, "path")
    add_files(project_path) 
    add_sqlflite_to_main(main_dart_path)


def add_files(project_path):
    providers_source_dir = os.path.join(os.getcwd(), "src","create_project","data","sqlflite")
    providers_destination_dir = os.path.join(project_path, "lib", "providers","sqlflite")
    
    os.makedirs(providers_destination_dir, exist_ok=True)
    
    # Copy each item (file or subfolder) from 'data/providers' to 'lib/providers'
    for item in os.listdir(providers_source_dir):
        source_item = os.path.join(providers_source_dir, item)
        destination_item = os.path.join(providers_destination_dir, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, destination_item)

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
    if not main_function_match:
        print("Could not find 'void main(){")
        return 
    
    insert_position_main = main_function_match.end()
    content = content[:insert_position_main] + sql_lite_main + content[insert_position_main:]

    if sqlflite_imports.strip() not in content:
        content = sqlflite_imports.strip() + content
    with open(main_dart_path, "w") as file:
        file.write(content)