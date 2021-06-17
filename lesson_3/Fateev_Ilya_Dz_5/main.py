import random


def get_jokes(n: int):
    """Получился весьма колхозный код, основанный на изменении содержимого списков"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    c = 4
    for i in range(n):
        count = random.randint(0, c)
        joke = " " + str(nouns[count])
        del nouns[count]
        count = random.randint(0, c)
        joke += " " + str(adverbs[count])
        del adverbs[count]
        count = random.randint(0, c)
        joke += " " + str(adjectives[count])
        del adjectives[count]
        print(joke)
        c -= 1


get_jokes(4)
