Текстовый генератор на основе N-грамм языковой модели

Все работает примерно так: 

1) Сначала мы добавляем нужный текст
2) Затем программа вычленяет из текста н-граммы нужной длинны и записывает всевозможные для них последующие слова слова примерно таким образом:  
    1) к каждой н-грамме присваивается список с количеством всех слова(включая повторения одинаковых) и словаря с последующими возможными словами и количеством каждого слова 
    2) словарь выглядит так: { ('pref word 1', 'pref word 2'...) : [20, {'next word 1':10, 'next word 2': 5, 'next word 3': 5]}]}
3) После этого программа проходит по словарю и вычисляет вероятность каждого последующего слова: (кол-во вхождений данного слова)/(кол-во всех слов, встречю после н-граммы)
    Например, для послученного выше словаря, окончательный словарь будет выглядеть так: 
    { ('pref word 1', 'pref word 2'...) : [('next word 1': 0.5), ('next word 2': 0.25), ('next word 3', 0.25)]}
4) Затем, идет генерация текста
5) Вводим начальные слова по размеру выбранной n-граммы, программа смотрит в словаре данную н-грамму и выбирает рандомно следующее слово (учитыая вероятности)

p.s. итоговый словарь запоминается в памяти в папке models