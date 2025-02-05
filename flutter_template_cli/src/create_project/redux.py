from .pubspec import modify_pubspec_yaml
import os
import shutil
import re

def add_redux_support(project_path,main_dart_path,is_interceptor_added):
    """Modifies the project to add Redux support."""

    os.makedirs(os.path.join(project_path, "lib", "providers"), exist_ok=True)

    # Add redux and flutter_redux to pubspec.yaml
    modify_pubspec_yaml(project_path, "flutter_redux")
    print("Added Redux support")
    add_files_to_providers(project_path,main_dart_path,is_interceptor_added)



def add_files_to_providers(project_path,main_dart_path,is_interceptor_added):
    if is_interceptor_added:
        #adding providers
        providers_source_dir = os.path.join(os.getcwd(), "src","create_project","data","providers")
        providers_destination_dir = os.path.join(project_path, "lib", "providers")
    
        os.makedirs(providers_destination_dir, exist_ok=True)
    
        # Copy each item (file or subfolder) from 'data/providers' to 'lib/providers'
        for item in os.listdir(providers_source_dir):
            source_item = os.path.join(providers_source_dir, item)
            destination_item = os.path.join(providers_destination_dir, item)
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, destination_item)

        #adding widgets
        widgets_source_dir = os.path.join(os.getcwd(), "src","create_project","data","widgets")
        widgets_destination_dir = os.path.join(project_path, "lib", "widgets")
    
        os.makedirs(widgets_destination_dir, exist_ok=True)
    
        # Copy each item (file or subfolder) from 'data/widgets' to 'lib/widgets'
        for item in os.listdir(widgets_source_dir):
            source_item = os.path.join(widgets_source_dir, item)
            destination_item = os.path.join(widgets_destination_dir, item)
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, destination_item)
        
        #adding interceptors
        interceptors_source_dir = os.path.join(os.getcwd(), "src","create_project","data","interceptors")
        interceptors_destination_dir = os.path.join(project_path, "lib", "services","interceptors")
    
        os.makedirs(interceptors_destination_dir, exist_ok=True)
    
        # Copy each item (file or subfolder) from 'data/interceptors' to 'lib/services/interceptors'
        for item in os.listdir(interceptors_source_dir):
            source_item = os.path.join(interceptors_source_dir, item)
            destination_item = os.path.join(interceptors_destination_dir, item)
            
            if os.path.isdir(source_item):
                # Copy subfolder to the destination
                shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
            else:
                # Copy individual file to the destination
                shutil.copy2(source_item, destination_item)
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
    if not main_function_match:
        print("Could not find 'void main(){")
        return 
    
    insert_position_main = main_function_match.end()
    content = content[:insert_position_main] + main_function_redux + content[insert_position_main:]
    
    #adding interceptor widgets
    interceptor_widgets = """
                    Loader(),
                    const ErrorDialog(),
"""
    stack_pattern = r"Stack\s*\(\s*children\s*:\s*\["
    stack_match = re.search(stack_pattern, content)
    if not stack_match:
        print("Could not find 'Stack(children: [' in main.dart.")
        return 

    insert_position = stack_match.end() 
    content = content[:insert_position] + interceptor_widgets + content[insert_position:]   


    if redux_imports.strip() not in content:
        content = redux_imports.strip() + content

    with open(main_dart_path, "w") as file:
        file.write(content)