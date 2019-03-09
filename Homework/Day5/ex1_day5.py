example_list = [1,2,3,4,-5, "one",6,7.5,8,9]

# list_sum = sum(example_list)
# print(list_sum)
only_number_list = []
error = ""

for i in example_list:
    if isinstance(i, int) or isinstance(i, float):
        only_number_list.append(i)

    else:
        error = "In your list is string, so I missed it and print sum only for numbers"
        continue


if len(error) > 0:
    print(error)
print(sum(only_number_list))
