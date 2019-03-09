number = int(input("Give me a number and I will check if it dividable by 3,5 or 7"))



if number % 3 == 0:
    print("Dividable by 3")
if number % 5 == 0:
    print("Dividable by 5")
if number % 7 == 0:
    print("Dividable by 7")
if number % 3 != 0 and number %5 != 0 or number % 7 != 0:
    print("Not Dividable")