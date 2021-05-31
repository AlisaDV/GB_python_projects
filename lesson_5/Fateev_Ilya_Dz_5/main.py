

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = {i: 0 for i in src}

for i in src:
    if(i in result):
        result[i]+=1

print([x for x in result if result[x]==1])


