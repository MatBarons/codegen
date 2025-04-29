from codegen.utils.config import Config
from .pubspec import modify_pubspec_yaml
from os import path,makedirs

def add_http_interceptor_support():
    project_path = Config().get("project_path")

    directory = path.join(project_path, "lib","services", "interceptors")
    makedirs(directory, exist_ok=True)

    # Add http_interceptor to pubspec.yaml
    modify_pubspec_yaml("http_interceptor")
    print("Added Redux support")