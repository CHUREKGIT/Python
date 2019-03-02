number = int(input("Give a number"))

if number < 100 and number >0:
 if number % 3 == 0:
   print("Fizz", end ="")
 if number % 5 == 0:
   print("Buzz")
 if number % 3 !=0 and number % 5 !=0:
   print(number)
else:
 print("Number should be more that 0 and less than 100")
