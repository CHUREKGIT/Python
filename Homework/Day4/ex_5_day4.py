#Fibonacci

number = range(0,101)
previus = []
for i in number:
    if i == 0:
        print(i)
        previus.append(i)
    if i == 1:
        print(i)
        previus.append(i)
    if i > 1:
        score = previus[-1] + previus[-2]
        print(score)
        previus.append(score)
