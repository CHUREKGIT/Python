number = int(input("Give me a number"))

table = []

for i in range(1,11):
    table.append(number * i)
    preformat_string = "{}," * 10

score = preformat_string.format(*table)

print(score)