import train
import generate


class NGramModel():
    seed = 2
    model_dir = ''
    n_word = {}

    def __init__(self, seed):
        self.seed = seed

    def fit(self, texts_dir=''):
        train.fit(self.seed, texts_dir)

    def generate(self, prefix, model_dir, length=20):
        self.model_dir = model_dir
        self.n_word = generate.load_model(model_dir)
        generate.generate(prefix, length, self.n_word, self.seed)
        return self


model = NGramModel(2)
model.fit('data')
model.generate('', 'models/data.pickle', 40)
