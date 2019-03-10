#Print numbers from 1 to 20. Only these that are not divided by 4.

to_20 = range(1, 21)

for i in to_20:
    if i % 4 == 0:
        continue
    else:
        print(i)
