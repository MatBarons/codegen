from inquirer import prompt,Text,List,Checkbox,Confirm,Path
from random import randbytes
def confirm(message):
    return prompt(Confirm(message=message,default=False))

def question(message):
    return prompt(Text(message=message))

def choose(message:str,choices:list,multiple:bool):
    if multiple:
        return prompt(Checkbox(message=message,choices=choices))
    else:
        return prompt(List(message=message,choices=choices))

def path(message:str):
    return prompt(Path(message=message,path_type=Path.DIRECTORY))
    
    