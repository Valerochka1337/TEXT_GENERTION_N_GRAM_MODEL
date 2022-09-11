import pickle
from numpy import random


def load_model(model_dir):
    with open('models/' + model_dir + '.pickle', 'rb') as f:
        n_word = pickle.load(f)
    return n_word


def generate(prefix='', length=10, n_word=None, ran_seed=23):
    # инициализируем сид
    random.seed(ran_seed)
    if n_word is None:
        n_word = {}
    # определяем длин н-грамм
    seed = len(list(n_word.keys())[0])
    text_ans = []
    # если пользователь не ввел начальные слова, то выбираем рандомно из n-грамм
    if prefix == '':
        for i in list(n_word.keys())[int(random.choice(len(list(n_word.keys()))))]:
            text_ans.append(i)
    # иначе разделяем введенные слова
    else:
        for w in prefix.split():
            text_ans.append(w.lower())
    for i in range(length):
        try:
            # тут, выбираем рандомно слово из возможных для данной n-граммы
            # учитываем вероятность каждого с помощью np.random.choice
            text_ans.append(n_word[tuple(text_ans[i:i + seed])][
                                int(random.choice(len(n_word[tuple(text_ans[i:i + seed])]), 1, p=list(
                                    map(lambda x: x[1], n_word[tuple(text_ans[i:i + seed])]))))][0])
        # если нет последующих слов, то завершаем с тем, что есть
        except Exception:
            print('not ehougth words')
            break

    print(*text_ans)
