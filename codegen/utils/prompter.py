from pathlib import Path
from InquirerPy import prompt
from InquirerPy.prompts import FuzzyPrompt

def confirm(message):
    return prompt([
        {
            "type": "confirm",
            "message": message,
            "name": "confirm",
            "default": False
        }
    ])["confirm"]

def question(message: str) -> str:
    return prompt([
        {
            "type": "input",
            "message": message,
            "name": "text"
        }
    ])["text"]

def choose(message: str, choices: list, multiple: bool):
    if multiple:
        return prompt([
            {
                "type": "checkbox",
                "message": message,
                "name": "selection",
                "choices": choices
            }
        ])["selection"]
    else:
        return prompt([
            {
                "type": "list",
                "message": message,
                "name": "selection",
                "choices": choices
            }
        ])["selection"]

def browse_dirs(message=None,current_path=Path.cwd().resolve()):
    if message is not None:
        print(message)

    dirs = sorted([d for d in current_path.iterdir() if d.is_dir()])
    choices = []

    # Add option to go up one directory level
    if current_path.parent != current_path:
        choices.append({"name": ".. (go up)", "value": ".."})

    # Add all subdirectories
    choices += [{"name": dir.name + "/", "value": dir.name} for dir in dirs]

    prompt = FuzzyPrompt(
        message=f"Current directory: {current_path}",
        choices=choices,
        multiselect=False,
        validate=lambda _: True,
    )
    @prompt.register_kb("alt-enter")
    def _handle_last_selection(event):
        if selected == "..":
            choice_value = current_path.parent
        else:
            choice_value= current_path / prompt.result_value
        event.app.exit(result=choice_value)
    selected = prompt.execute()
    if selected is not None:
        if selected == "..":
            browse_dirs(current_path=current_path.parent)
        else:
            browse_dirs(current_path=current_path / selected)
    else:
        return selected
    
        
