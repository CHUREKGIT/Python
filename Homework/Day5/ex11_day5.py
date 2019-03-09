my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]

for i in sorted(set(my_list)):
    print(f"{i} is in this list {my_list.count(i)} times")

