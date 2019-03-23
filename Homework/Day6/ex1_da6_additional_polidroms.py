#polidromes
import math

x = int(input("Give me first number from range"))
y = int(input("Give me last number from range"))

polidroms = []
fair_and_square = []

for number in range(x,(y+1)^2):
    if number in range(1, 10):
        polidroms.append(number)
    if number >= 10 and str(number)[::-1] == str(number):
        polidroms.append(number)


for number in range(x,y+1):
    if (math.sqrt(number) in polidroms) and str(number)[::-1] == str(number):
        fair_and_square.append(number)



print(f"Fair and square in this range: {fair_and_square}")