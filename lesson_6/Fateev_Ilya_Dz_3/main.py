import json
from itertools import zip_longest

while 1:
    path_u = input()
    path_h = input()
    path_r = input()
    print(path_u)
    print(path_h)
    print(path_r)
    try:
        f_users = open(path_u, "r", encoding="utf-8")
        f_hobby = open(path_h, "r", encoding="utf-8")
        f_result = open(path_r, "w", encoding="utf-8")
        break
    except FileNotFoundError:
        print("Path is wrong. Enter correct path")
        continue


if len(f_users.readlines())>len(f_hobby.readlines()):
    result = zip_longest((user for user in f_users), f_hobby, fillvalue=None)
    res = {str(element[0]).strip(): (element[1].strip()) for element in result}

    json.dump(res, f_result, ensure_ascii=False, indent=4)
else:
    exit(1)

f_result.close()
f_hobby.close()
f_users.close()

