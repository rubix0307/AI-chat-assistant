from GPT.config import assistant, client, thread
from GPT.functions import take_question







if __name__ == '__main__':


    input_text = True
    while input_text:
        input_text = input('Enter a question: ')
        print(take_question(client, assistant, thread, input_text))


    print()

