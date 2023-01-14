i = input('Enter ten numbers : ')
list1 = [int(x) for x in i.split()]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print('The distinct numbers are: ', list2)
