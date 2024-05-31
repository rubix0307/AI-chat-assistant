import random


def get_current_weather(location=None, *args, **kwargs):
    tmp = random.randint(0,36)
    print(f'{tmp=}')
    return tmp



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
    }
]