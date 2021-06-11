def setQuotes(li: list, mess: list):
    count = 0
    for i in li:
        print(i)
        mess.insert(i + count, '"')
        count += 2
        mess.insert(i + count, '"')


def findNum(li: list):
    nums = []
    count = -1
    while count < len(li):
        try:
            type(int(li[count]))
            nums.append(count)
            count += 1
        except ValueError:
            count += 1
            continue
    return(nums)




message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

setQuotes(findNum(message), message)
x = " "
myStr = x.join(message)
print(myStr)
