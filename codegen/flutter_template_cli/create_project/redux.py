from re import search
from os import makedirs,path
from codegen.utils.config import Config

from .pubspec import modify_pubspec_yaml
from codegen.utils.utils import copy_folders,write_file,get_flutter_data

def add_redux_support(is_interceptor_added):

    project_path = Config().get("project_path")

    """Modifies the project to add Redux support."""

    makedirs(path.join(project_path, "lib", "providers"), exist_ok=True)

    # Add redux and flutter_redux to pubspec.yaml
    modify_pubspec_yaml("flutter_redux")
    print("Added Redux support")
    if is_interceptor_added:
        add_files_to_providers()

def add_files_to_providers():
    project_path = Config().get("project_path")
    #adding providers
    providers_source_dir = path.join(get_flutter_data(),"create","providers")
    providers_destination_dir = path.join(project_path, "lib", "providers")
    copy_folders(providers_source_dir,providers_destination_dir)

    #adding widgets
    widgets_source_dir = path.join(get_flutter_data(),"create","widgets")
    widgets_destination_dir = path.join(project_path, "lib", "widgets")
    copy_folders(widgets_source_dir,widgets_destination_dir)

    #adding interceptors
    interceptors_source_dir = path.join(get_flutter_data(),"create","interceptors")
    interceptors_destination_dir = path.join(project_path, "lib", "services","interceptors")
    copy_folders(interceptors_source_dir,interceptors_destination_dir)
    
    add_redux_to_main()
        
def add_redux_to_main():
    project_path = Config().get("project_path")
    main_dart_path = path.join(project_path, "lib", "main.dart")
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
    main_function_match = search(main_function_pattern,content)
    content = write_file(main_function_match,main_function_redux,content)
    
    #adding interceptor widgets
    interceptor_widgets = """
                    Loader(),
                    const ErrorDialog(),
"""
    stack_pattern = r"Stack\s*\(\s*children\s*:\s*\["
    stack_match = search(stack_pattern, content)
    content = write_file(stack_match,interceptor_widgets,content)


    if redux_imports.strip() not in content:
        content = redux_imports.strip() + content

    with open(main_dart_path, "w") as file:
        file.write(content)