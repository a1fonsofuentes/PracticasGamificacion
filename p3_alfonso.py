list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in list1:
    if i == list1[4] or i == list1[7] or i == list1[9]:
        a = i * 2
        list2.append(a)
print(list2)        
