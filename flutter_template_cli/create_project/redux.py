import os
import re

from .pubspec import modify_pubspec_yaml
from utils.utils import copy_folders,write_file

def add_redux_support(project_path,main_dart_path,is_interceptor_added):
    """Modifies the project to add Redux support."""

    os.makedirs(os.path.join(project_path, "lib", "providers"), exist_ok=True)

    # Add redux and flutter_redux to pubspec.yaml
    modify_pubspec_yaml(project_path, "flutter_redux")
    print("Added Redux support")
    if is_interceptor_added:
        add_files_to_providers(project_path,main_dart_path)



def add_files_to_providers(project_path,main_dart_path):
    #adding providers
    providers_source_dir = os.path.join(os.getcwd(), "src","create_project","data","providers")
    providers_destination_dir = os.path.join(project_path, "lib", "providers")
    copy_folders(providers_source_dir,providers_destination_dir)

    #adding widgets
    widgets_source_dir = os.path.join(os.getcwd(), "src","create_project","data","widgets")
    widgets_destination_dir = os.path.join(project_path, "lib", "widgets")
    copy_folders(widgets_source_dir,widgets_destination_dir)

    #adding interceptors
    interceptors_source_dir = os.path.join(os.getcwd(), "src","create_project","data","interceptors")
    interceptors_destination_dir = os.path.join(project_path, "lib", "services","interceptors")
    copy_folders(interceptors_source_dir,interceptors_destination_dir)
    
    add_redux_to_main(main_dart_path)
        
def add_redux_to_main(main_dart_path):
    
    with open(main_dart_path, "r") as file:
        content = file.read()
    
    redux_imports = """
import 'package:flutter_redux/flutter_redux.dart';
import 'package:redux/redux.dart';
import 'providers/redux_store.dart';
import 'providers/app_state/app_state.dart';
import 'providers/app_state/reducers/app_reducers.dart';
import 'widgets/error.dart';
import 'widgets/loader.dart';"""
    
    
    #adding main function store 
    main_function_redux = """
    ReduxStoreManager().init(
        Store<AppState>(appReducer, initialState: AppState.initial()),
    );
"""
    main_function_pattern = r"void\s+main\s*\(\s*\)\s+async\s*\{"
    main_function_match = re.search(main_function_pattern,content)
    write_file(main_function_match,main_function_redux)
    
    #adding interceptor widgets
    interceptor_widgets = """
                    Loader(),
                    const ErrorDialog(),
"""
    stack_pattern = r"Stack\s*\(\s*children\s*:\s*\["
    stack_match = re.search(stack_pattern, content)
    write_file(stack_match,interceptor_widgets)


    if redux_imports.strip() not in content:
        content = redux_imports.strip() + content

    with open(main_dart_path, "w") as file:
        file.write(content)