#palidromes
import math

x = int(input("Give me first number from range"))
y = int(input("Give me last number from range"))

palidroms = []
fair_and_square = []

for number in range(round(math.sqrt(x)),y+1):
    if number in range(1, 10):
        palidroms.append(number)
    if number >= 10 and str(number)[::-1] == str(number):
        palidroms.append(number)


for number in range(x,y+1):
    if (math.sqrt(number) in palidroms) and str(number)[::-1] == str(number):
        fair_and_square.append(number)



print(f"Fair and square in this range: {fair_and_square}")