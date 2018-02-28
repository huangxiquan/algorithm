dict = [3,6,1,8,5,2,9,4]
for index,x in enumerate(dict):
    for i, y in enumerate(dict[:len(dict) - index - 1]):
        print(y)
        if(dict[i] > dict[i + 1]):
            temp = dict[i]
            dict[i] = dict[i + 1]
            dict[i + 1] = temp
print(dict)
