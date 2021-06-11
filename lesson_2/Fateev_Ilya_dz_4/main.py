

staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in staff:
    *position, name = i.split()
    print("Hello ", name.casefold().title())
