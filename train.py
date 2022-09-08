import re
import pickle
import os


def fit(seed=2, data_dir='data'):
    text = ''
    for filename in os.listdir(data_dir):
        with open(os.path.join(data_dir, filename), 'r', encoding='UTF-8') as f:
            text += ' ' + f.read().lower()

    text = [i for i in re.findall(r'\w+', text)]

    print('Number of words:', len(text))
    n_word = {}

    for i in range(len(text) - seed):
        if not n_word.__contains__(tuple(text[i:i + seed])):
            n_word[tuple(text[i:i + seed])] = [1, {text[i + seed]: 1}]
        else:
            if text[i + seed] in n_word[tuple(text[i:i + seed])][1]:
                n_word[tuple(text[i:i + seed])][1][text[i + seed]] += 1
            else:
                n_word[tuple(text[i:i + seed])][1][text[i + seed]] = 1
            n_word[tuple(text[i:i + seed])][0] += 1

    for pref in n_word.keys():
        probs = []
        for i in n_word[pref][1].keys():
            probs.append([i, n_word[pref][1][i] / n_word[pref][0]])
        n_word[pref] = probs

    with open('models/data.pickle', 'wb') as f:
        pickle.dump(n_word, f)
