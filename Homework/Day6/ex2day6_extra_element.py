#SETS WAY
# list_a = [1,5,2,8,3,11,15]
# list_b = [5,15,1,2,8,11,12,3]
#
# def extra_el(list_a, list_b):
#  set_a = set(list_a)
#  set_b = set(list_b)
#
#  return set_a ^ set_b
#
#
# results = extra_el(list_a, list_b)
# print(f"Extra element from these lists is {results}")


#FOR Way
list_a = [1,5,2,8,3,11,15]
list_b = [5,15,1,2,8,11,3,77]

def extra_el(list_a, list_b):
    extra = set()
    for i in list_a:
        if i not in list_b:
            extra.add(i)
    for i in list_b:
        if i not in list_a:
            extra.add(i)
    return extra

results = extra_el(list_a, list_b)
print(f"Extra element from these lists is {results}")


