import pickle
from random import choice
from numpy import random


# prefix = ()
# seed = 3
# model_dir = ''
# length = 10
# n_word = {}

def load_model(model_dir):
    with open(model_dir, 'rb') as f:
        n_word = pickle.load(f)
    return n_word


def generate(prefix=(), length=10, n_word=None, seed=2):
    if n_word is None:
        n_word = {}
    text_ans = []
    for i in choice(list(n_word.keys())):
        text_ans.append(i)
    for i in range(length):
        try:
            # залупа не пытыйтесь понять, но оно (РЕАЛЬНО!!!!) работает
            text_ans.append(n_word[tuple(text_ans[i:i + seed])][
                                int(random.choice(len(n_word[tuple(text_ans[i:i + seed])]), 1, p=list(
                                    map(lambda x: x[1], n_word[tuple(text_ans[i:i + seed])]))))][0])
        except Exception:
            print('not ehougth words')
            break

    print(*text_ans)
