import random

def showPrice(li: list):
    part = 0
    for i in li:
        part = int(i)
        if (int(i) < 10):
            part = "0"
            part += str(int(i))
        print(part, "руб", round((i - int(i)) * 100), "коп")


price = []
for i in range(20):
    price.append(round(random.random() * 100, 2))


#Task №1
showPrice(price)
print("------------------------\n")

#Task №2
showPrice(sorted(price))
print("\n")
showPrice(price)
print("-------------------------\n")

#Task №3
priceReverse = [x for x in price]
priceReverse.sort(reverse = True)
showPrice(priceReverse)
print("-------------------------\n")

#Task №4
showPrice(sorted(price)[-5:])
