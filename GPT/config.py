from openai import OpenAI
from GPT.tools import tools_description
import config

client = OpenAI()
instructions = 'Ты должен отвечать как настоящий человек и отвечать в JSON режиме, а именно: {"content": твой ответ}'
assistant = client.beta.assistants.create(model='gpt-4o', tools=tools_description, instructions=instructions)
assistant_id = assistant.id

# todo make function for getting thread by user_id
thread = client.beta.threads.create()
thread_id = thread.id