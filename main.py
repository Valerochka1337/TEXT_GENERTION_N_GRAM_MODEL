import train
import generate


# клас модели
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


# Консольный итерфейс:

if __name__ == '__main__':
    inp = ''
    print('---Thank you for using this program!---', '---Description:',
          '------Comands: fit(training), generate(text generation), exit', sep='\n')
    while inp != 'exit':
        inp = input('---Enter comand: ')
        if inp == 'fit':
            seed = int(input('------Enter seed (number of words):'))
            model = NGramModel(seed)
            data = input('------Enter data folder name:')
            print('-----------------loading----------------')
            model.fit(data)
            print('--------model is fitted and saved-------')

        elif inp == 'generate':
            pref = input('------Enter start words (leave blank to use randomly generated):')
            model_path = input('------Enter model name:')
            length = int(input('------Enter length of the generated text:'))
            model.generate(pref, model_path, length)
        else:
            print('----------------------------------------')
    else:
        print('Thank you for using our product!')
