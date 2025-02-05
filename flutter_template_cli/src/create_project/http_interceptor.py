from .pubspec import modify_pubspec_yaml
import os

def add_http_interceptor_support(project_path):

    directory = os.path.join(project_path, "lib","services", "interceptors")
    os.makedirs(directory, exist_ok=True)

    # Add http_interceptor to pubspec.yaml
    modify_pubspec_yaml(project_path, "http_interceptor")
    print("Added Redux support")