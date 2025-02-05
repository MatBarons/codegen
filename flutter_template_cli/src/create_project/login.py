from .pubspec import modify_pubspec_yaml


def add_login_support(project_path, login_type,main_dart_path):
    """Modifies the project to add specific login support."""
    if login_type == "keycloak":
        modify_pubspec_yaml(project_path, "keycloak_flutter")
        #add_keycloak_to_main()
    elif login_type == "azure":
        modify_pubspec_yaml(project_path, "msal_flutter")
        #add_azure_to_main()
    elif login_type == "cognito":
        modify_pubspec_yaml(project_path, "amazon_cognito_identity_dart_2")
        #add_cognito_to_main()
    elif login_type == "magic":
        modify_pubspec_yaml(project_path, "magic_sdk")
        #add_magic_to_main()

