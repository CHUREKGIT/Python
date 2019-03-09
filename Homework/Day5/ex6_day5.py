lista_a = [10,20,30,20,10,50,60,40,80,50,40]
new_list = sorted(lista_a)
dup_list = []
unique_list = []

for i in range(len(new_list)):
    if lista_a.count(new_list[i]) > 1:
        dup_list.append(new_list[i])

for i in lista_a:
    if i not in dup_list:
        unique_list.append(i)

print(unique_list)
