# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
#
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes_adv(count: int, flag=False) -> list:
    """ Функция создана для выборки случаных элементов из вышеуказанных списков;
     В последующем объединяняя эти элемнты в один список"""
    list_out = []
    for i in range(count):
        nouns_1 = choice(nouns)
        adverbs_1 = choice(adverbs)
        adjectives_1 = choice(adjectives)
        humor = f'{nouns_1} {adverbs_1} {adjectives_1}'
        list_1 = []
        # print(humor)
        list_out.append(humor)
        if flag == True:
            list_1 = humor.split()
            for nouns_2 in nouns:
                for joke in list_1:
                    if nouns_2 == joke:
                        nouns.remove(nouns_2)
            for adverbs_2 in adverbs:
                for joke_1 in list_1:
                    if adverbs_2 == joke_1:
                        adverbs.remove(adverbs_2)
            for adjectives_2 in adjectives:
                for joke_2 in list_1:
                    if adjectives_2 == joke_2:
                        adjectives.remove(adjectives_2)
    return list_out


print(get_jokes_adv(4, flag=True))
