import json
from openai.types.beta.threads.run_submit_tool_outputs_params import ToolOutput
from openai.resources.beta.threads.runs import Runs
from GPT.tools import *
from GPT.config import client







def get_response(thread_id):
  messages = client.beta.threads.messages.list(thread_id=thread_id)
  message_content = messages.data[0].content
  if message_content:
      message_content = message_content[0].text

      annotations = message_content.annotations
      for annotation in annotations:
        message_content.value = message_content.value.replace(annotation.text, '')

      response_message = message_content.value
      return response_message
  return None


def take_question(client, assistant_id, thread_id, question=None, run_data=None):

    if run_data:
        run = Runs(client=client).poll(run_id=run_data.id, thread_id=run_data.thread_id)
    else:
        if question:
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread_id, assistant_id=assistant_id, poll_interval_ms=2000,
                additional_messages=[{'content': question, 'role': 'user'}]
            )
        else:
            return None


    if run.status == "completed":
        response_message = get_response(run.thread_id)
        return response_message

    elif run.status == 'requires_action':
        if run.required_action.submit_tool_outputs.tool_calls:
            tool_outputs = []
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                function_data = tool_call.function

                f = globals().get(function_data.name)
                if f:
                    arguments = json.loads(function_data.arguments)
                    response_message = f(**arguments)
                    tool_outputs.append(
                        ToolOutput(output=str(response_message), tool_call_id=tool_call.id)
                    )

            if tool_outputs:
                submit_tool = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=run.thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs)

                return take_question(
                    client,
                    assistant_id,
                    thread_id,
                    run_data=submit_tool,
                )
            return False

