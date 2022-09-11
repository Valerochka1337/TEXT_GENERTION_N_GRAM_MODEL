import train
import generate


# клас модели
class NGramModel():
    seed = 2
    model_dir = ''
    n_word = {}

    def fit(self, texts_dir='', seed=2, model=''):
        train.fit(seed, texts_dir, model)

    def generate(self, prefix, model_dir, length=20, ran_seed=23):
        self.model_dir = model_dir
        self.n_word = generate.load_model(model_dir)
        generate.generate(prefix, length, self.n_word, ran_seed)
        return self


# Консольный итерфейс:

if __name__ == '__main__':
    inp = ''
    print('------Comands: fit(training), generate(text generation), exit', sep='\n')
    model = NGramModel()
    while inp != 'exit':
        inp = input('---Enter comand: ')
        if inp == 'fit':
            seed = int(input('------Enter seed (number of words):'))
            data = input('------Enter data folder name:')
            model_dir = input('------Enter model name:')
            print('-----------------loading----------------')
            model.fit(data, seed, model_dir)
            print('--------model is fitted and saved-------')

        elif inp == 'generate':
            model_path = input('------Enter model name:')
            ran_seed = int(input('------Enter random seed:'))
            pref = input('------Enter start words (leave blank to use randomly generated):')
            length = int(input('------Enter length of the generated text:'))
            model.generate(pref, model_path, length, ran_seed)
        else:
            print('----------------------------------------')
