import random
from openai.resources.beta.assistants import Assistants
from openai.types.beta.assistant import Assistant

from config import self_instructions_line


def update_instructions(instructions,*, client, assistant, **kwargs) -> Assistant:

    base_instructions, *self_instructions = assistant.instructions.split(self_instructions_line)
    new_instructions = '\n'.join([
        base_instructions,
        self_instructions_line,
        instructions,
    ]).replace('\n'*3,'')

    print(f'> New instructions: \n{instructions}')

    new_assistant = Assistants(client=client).update(
        assistant_id=assistant.id,
        instructions=new_instructions,
    )
    assistant.instructions = new_assistant.instructions
    return assistant

def get_current_weather(location=None, *args, **kwargs):
    tmp = random.randint(0,36)
    print(f'{tmp=}')
    return {'location': location, 'temperature': tmp}



tools_description = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Получение текущей погоды в заданном городе",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Город, например: Киев, Милан",
                    },
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_instructions",
            "description": "Обновление своей инструкции",
            "parameters": {
                "type": "object",
                "properties": {
                    "instructions": {
                        "type": "string",
                        "description": "Список новых данных для инструкций",
                    },
                },
                "required": ["location"],
            },
        },
    },
]