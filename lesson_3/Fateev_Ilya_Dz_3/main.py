import collections
def thesaurus(*names):
    names_groups = {}
    for name in names:
        key = name[0].title()
        if key not in names_groups:
            names_groups[key] = []
        names_groups[key].append(name)

    return names_groups


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
