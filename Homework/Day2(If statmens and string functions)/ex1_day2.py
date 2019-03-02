# ZADANKO 1
var = input("Give me 9 characters o or x")

# sprawdzamy piony
if var[0] == var[3] == var[6] or var[2] == var[5] == var[8]:
    print("WIN!!!!")
# sprawdzam rząd
elif var[0:3] =="xxx" or var[0:3] =="ooo" or var[3:5] =="xxx" or var[3:5] =="ooo" or var[6:8]=="xxx" or var[6:8]=="ooo":
    print("WIN!!!")
#sprawdzam skos
elif var[0] == var[4] == var[8] or var[2] == var[4] == var[6]:
    print("WIN")
else:
    print("LOSE")
