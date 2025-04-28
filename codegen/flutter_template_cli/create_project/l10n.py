import os
import re
import shutil

from codegen.utils.utils import write_file, get_flutter_data
from .pubspec import modify_pubspec_yaml

def add_l10n_support(project_path, languages,main_dart_path):
    """Modifies the project to add l10n (localization) support."""


    add_generate_flag(project_path)
    # Create l10n.yaml configuration file
    l10n_config_path = os.path.join(project_path, "l10n.yaml")
    with open(l10n_config_path, "w") as file:
        file.write("arb-dir: lib/l10n\n")
        file.write("template-arb-file: app_en.arb\n")
        file.write("output-localization-file: app_localizations.dart\n")
    print(f"Localization configuration added to {l10n_config_path}")

    data_l10n_dir = os.path.join(get_flutter_data(),"create", "l10n")
    l10n_dir = os.path.join(project_path, "lib", "l10n")

    if not os.path.exists(data_l10n_dir):
        print(f"Error: Source l10n folder '{data_l10n_dir}' does not exist.")
        return

    # Remove the target folder if it exists to ensure a clean copy
    if os.path.exists(l10n_dir):
        shutil.rmtree(l10n_dir)

    # Copy the l10n folder
    shutil.copytree(data_l10n_dir, l10n_dir)

    
    for lang in languages:
        lang_code = lang.strip()
        if not (lang_code == 'en' or lang_code == 'it'):
            arb_file_path = os.path.join(l10n_dir, f"app_{lang_code}.arb")
            with open(arb_file_path, "w") as file:
                file.write('{\n  "@@locale": "' + lang_code + '"\n}\n')
            print(f"Added localization file: {arb_file_path}")

    modify_pubspec_yaml(project_path, "intl")
    modify_pubspec_yaml(project_path, """flutter_localizations:
        sdk: flutter #""")
    add_l10n_to_main(languages,main_dart_path)

def add_generate_flag(project_path):
    pubspec_path = os.path.join(project_path, "pubspec.yaml")

    if not os.path.exists(pubspec_path):
        raise FileNotFoundError(f"pubspec.yaml not found at {pubspec_path}")

    # Read the existing content of pubspec.yaml
    with open(pubspec_path, "r") as file:
        lines = file.readlines()

    flutter_section_index = None
    for i, line in enumerate(lines):
        # Locate the standalone "flutter:" section
        if line.strip() == "flutter:":
            # Check if the previous line contains "dependencies:"
            if i > 0 and not("dependencies:" in lines[i - 1]):
                flutter_section_index = i
                break

    generate_flag = "  generate: true\n"

    if flutter_section_index is not None:
        # Check if "generate: true" already exists in the "flutter:" section
        for j in range(flutter_section_index + 1, len(lines)):
            # Break if a new section starts
            if not lines[j].startswith(" "):
                break
            if "generate:" in lines[j]:
                print("The 'generate: true' flag already exists. No changes made.")
                return

        # Find where to insert the new flag
        insert_index = flutter_section_index + 1
        while insert_index < len(lines) and lines[insert_index].startswith(" "):
            insert_index += 1

        # Insert "generate: true" after the flutter: section
        lines.insert(insert_index, generate_flag)
    else:
        # If the flutter section doesn't exist, add it at the end of the file
        if not lines[-1].endswith("\n"):
            lines.append("\n")  # Ensure the file ends with a newline
        lines.append("flutter:\n")
        lines.append(generate_flag)

    # Write the updated content back to pubspec.yaml
    with open(pubspec_path, "w") as file:
        file.writelines(lines)

    print(f"'generate: true' flag added successfully to {pubspec_path}")


def add_l10n_to_main(languages,main_dart_path):
    """Modifies main.dart file to add l10n support."""
    with open(main_dart_path, "r") as file:
        content = file.read()

    l10n_imports = """
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';\n
"""

    delegates = """
            localizationsDelegates: const [
                AppLocalizations.delegate,
                GlobalMaterialLocalizations.delegate,
                GlobalWidgetsLocalizations.delegate,
                GlobalCupertinoLocalizations.delegate,
            ],
    """
    delegates_pattern = r"MaterialApp\s*\("
    delegates_match = re.search(delegates_pattern,content, re.DOTALL)
    content = write_file(delegates_match,delegates,content)
    
    languages.append('en')
    languages.append('it')
    locales_list = ",\n          ".join([f"Locale('{lang.strip()}')" for lang in languages])

    # Define the supportedLocales content
    supported_locales_content = f"supportedLocales: const [\n          {locales_list},\n        ],"

    # Regex pattern to locate MaterialApp and look for supportedLocales
    material_app_pattern = r"(MaterialApp\s*\(.*?)(supportedLocales\s*:.*?,)?"
    
    # Search for the MaterialApp widget in main.dart
    match = re.search(material_app_pattern, content, re.DOTALL)

    if match:
        # Insert supportedLocales inside the MaterialApp if not already present
        if not match.group(2):
            # Get the insertion position just after MaterialApp(
            insert_position = match.end(1)
            content = content[:insert_position] + "\n        " + supported_locales_content + content[insert_position:]
        else:
            print("supportedLocales already exists. Skipping insertion.")
    else:
        print("Could not find MaterialApp in main.dart.")
        return

    if l10n_imports.strip() not in content:
        content = l10n_imports.strip() + content

    # Write the modified content back to main.dart
    with open(main_dart_path, "w") as file:
        file.write(content)

    print("supportedLocales added to main.dart based on user selection.")
    