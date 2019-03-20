#reverse example list

lista_a = [1,2,3,4,5,61,23]
lista_b =[]
def reverse(lista_a):


    for i in range(1,len(lista_a)+1):
        lista_b.append(lista_a[-i])

    print(lista_b)

reverse(lista_a)