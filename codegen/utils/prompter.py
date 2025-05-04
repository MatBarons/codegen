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
        choices.append({"name": ".. (go up)", "value": {"value":"..","should_exit": False}})

    # Add all subdirectories
    choices += [{"name": dir.name + "/", "value": {"value": dir.name, "should_exit": False}} for dir in dirs]

    prompt = FuzzyPrompt(
        message=f"Current directory: {current_path}",
        choices=choices,
        multiselect=False,
        validate=lambda _: True,
    )
    @prompt.register_kb("alt-enter")
    def _handle_last_selection(event):
        choice_value = prompt.result_value["value"]
        if choice_value == "..":
            event.app.exit(result={"value": current_path.parent, "should_exit": True})
        else:
            event.app.exit(result={"value": current_path / choice_value, "should_exit": True})
    
    selected = prompt.execute()
    print(selected)
    if selected["should_exit"] is False:
        if selected["value"] == "..":
            return browse_dirs(current_path=current_path.parent)
        else:
            return browse_dirs(current_path=current_path / selected["value"])
    else:
        return selected["value"]
    
        
