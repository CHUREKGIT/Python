temperature = input("Give a temperature")
number = int(temperature[:-1])

if temperature[-1] == "F":

    celcius = round((number - 32) * (5/9))

    print("This temperature in " + temperature[-1] + " is " + str(celcius) + "C")
else:
    farenheit = round(number  * (9/5) + 32)

    print ("This temprature in " + temperature[-1] + " is " + str(farenheit) + "F")