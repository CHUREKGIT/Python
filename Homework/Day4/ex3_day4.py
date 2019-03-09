#count how many numbers

parzyste = 0
nieparzyste = 0


numbers_range = range(1, 10)

for i in numbers_range:
    if i % 2 ==0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'przystych is {parzyste}')
print(f'nieparzyste is {nieparzyste}')