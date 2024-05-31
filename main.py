from GPT.config import assistant_id, client, thread_id
from GPT.functions import take_question







if __name__ == '__main__':
    start_question = 'Какая сумма температур в трех европейских столицах? Выбери их на свое усмотрение'
    print(take_question(client, assistant_id, thread_id, start_question))