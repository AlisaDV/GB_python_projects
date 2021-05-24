def num_translate_adv(s: str):
    nums = {'Zero': 'ноль', 'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре', 'Five': 'пять',
         'Six': 'шесть', 'Seven': 'семь', 'Eight': 'восемь', 'Nine': 'девять', 'Ten': 'десять'}
    if s[0].istitle():
        num_ru = nums.get(s)
        return num_ru.title()
    else:
        num_ru = nums.get(s.title())
        return num_ru


print(num_translate_adv(input()))
