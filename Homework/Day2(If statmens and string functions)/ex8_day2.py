a = int(input("Give me a number 1"))
b = int(input("Give me a number 2"))
c = int(input("Give me a number 3"))


if a+b > c and a+c > b and b+c > a:

    if  a==b==c:
        print("This traingle is equilateral")
    elif a==b or a==c or b==c:
        print("This traingle is isosceles")
    else:
        print("This is traingle")

else:
    print("I can't build traingle from this number")