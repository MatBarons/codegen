from inquirer import prompt,Text,List,Checkbox,Confirm,Path

def confirm(message):
    return prompt([Confirm(name='confirm',message=message,default=False)]).get('confirm')

def question(message):
    return prompt([Text(name='text',message=message)]).get('text')

def choose(message:str,choices:list,multiple:bool):
    if multiple:
        return prompt([Checkbox(name='checkbox',message=message,choices=choices)]).get('checkbox')
    else:
        return prompt([List(name='list',message=message,choices=choices)]).get('list')

def directory(message:str):
    return prompt([Path(name='path',message=message,path_type=Path.DIRECTORY)]).get('path')
    
    