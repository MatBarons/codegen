import os

def modify_pubspec_yaml(project_path, package_name):
    """Adds a package to the dependencies section of pubspec.yaml if it exists, 
    or creates the dependencies section if it doesn't."""
    
    pubspec_path = os.path.join(project_path, "pubspec.yaml")
    
    # Read the existing content of pubspec.yaml
    with open(pubspec_path, "r") as file:
        lines = file.readlines()

    # Check if "dependencies:" already exists
    dependencies_index = next((i for i, line in enumerate(lines) if line.strip() == "dependencies:"), None)

    # If "dependencies:" section exists, append the package under it
    if dependencies_index is not None:
        insert_index = dependencies_index + 1
        while insert_index < len(lines) and (lines[insert_index].startswith(" ") or not lines[insert_index].strip()):
            insert_index += 1
        lines.insert(insert_index, f"  {package_name}: \n")

    # If "dependencies:" doesn't exist, add it at the end
    else:
        lines.append("\ndependencies:\n")
        lines.append(f"  {package_name}: \n")

    with open(pubspec_path, "w") as file:
        file.writelines(lines)

    print(f"Added {package_name} to {pubspec_path}")

