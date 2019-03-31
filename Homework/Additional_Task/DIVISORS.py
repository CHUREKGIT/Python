#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("Give me a number under 1000"))
range = range (1,1001)
divisor = []

for i in range:
    if number % i == 0:
        divisor.append(i)
print(f"Divisor for you number are: {divisor}")