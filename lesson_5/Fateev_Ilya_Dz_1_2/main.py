
#Task 1
def gen():
    for i in range(0, 16):
        if i % 2 != 0:
            yield i


for j in gen():
    print(j)


#Task 2
print(*(x for x in range(0, 16) if x % 2 != 0))

