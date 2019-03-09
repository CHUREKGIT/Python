number = int(input("Give me a number between 1 and 36 "));

if number >=1 and number <= 36:

    if number % 2 != 0 and (number >= 1 and number <= 10) or (number >=19 and number <= 28):
        print("red\nodd")
    elif number % 2 == 0 and (number >= 1 and number <= 10) or (number >=19 and number <= 28):
        print("black\neven")
    elif number % 2 != 0 and (number >= 11 and number <= 18) or (number >=29 and number <= 36):
        print("black\nodd")
    else:
        print("red\neven")
    if number <= 18:
        print("low")
    else:
        print("high")
else:
    print("Wrong number")