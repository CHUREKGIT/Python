lst_a = [1,2,3,4,5,6]
lst_b = [6,7,9,10,6]

list_c = set(lst_a) & set(lst_b)

if len(list_c) > 0:
    print(True)
else:
    print(False)


