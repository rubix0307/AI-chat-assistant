from GPT.config import assistant_id, client, thread_id
from GPT.functions import take_question







if __name__ == '__main__':
    start_question = 'Какая сумма температур в Минске, Москве и Киеве?'
    print(take_question(client, assistant_id, thread_id, start_question))