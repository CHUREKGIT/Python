#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Give me your name")
age = int(input("Give me your age"))

lack = 100 - age
year_when_user_100yearold = 2019 + (100 - age)

print(f"{name} you will be 100 year old in {year_when_user_100yearold}")
