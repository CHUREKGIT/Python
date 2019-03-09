lst_a = [1,2,3,4,5, "fire"]
lst_b = [6,7,"fire",9,10]


for i in lst_a:
    if i in set(lst_b):
        print(True)
