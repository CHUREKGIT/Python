month = input("Give me a month")
day = int(input("Give me a day"))

if (day >= 1 and day <= 31) and month in('January'
'February'
'March'
'April'
'May'
'June'
'July'
'August'
'September'
'October'
'November'
'December'):
    if (day >=20 and month == 'March') or month in('April','May') or(day <= 20 and month == 'June'):
        print("Spring")
    elif (day >= 21 and month == "June") or month in ('July', 'August') or (day <= 21 and month == 'September'):
        print('Summer')
    elif (day >= 22 and month == 'September') or month in ('October', 'November') or (day <= 20 and month == 'December'):
        print ('Autumn')
    else:
        print('Winter')
else:
    print('Number should be between 1 and 31 and month should be month :)')
