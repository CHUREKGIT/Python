year = int(input("Give me a year"))

if year % 4 == 0:
    print("This is leap year")
elif year % 100 != 0 and year % 400 == 0:
    print("This is leap year")
else:
    print("This is not leap year")