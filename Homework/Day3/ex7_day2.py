month = input("Give me a month name")


if month.upper() in ('SEPTEMBER','APRIL', 'JUNE', 'NOVEMBER'):
    print("This month has 30 days")
elif month.upper() == 'FEBRUARY':
    print("This month has 28 days and 29 in leap year")
else:
    print('This month has 31 days')