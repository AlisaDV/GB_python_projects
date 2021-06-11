import pymorphy2


morph = pymorphy2.MorphAnalyzer()
percent = morph.parse('процент')[0]
print(percent.make_agree_with_number(int(input())).word)
