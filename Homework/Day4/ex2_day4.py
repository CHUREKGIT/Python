height = int(input("Give me a height"))

spaces = " " * (height - 1)
first_line = spaces + "*"

for i in range (1, height+1):
    if i == 1:
        print(first_line)
    else:
        lines = "*" * (2 * i - 1)
        spaces = spaces[:-1]
        print(f"{spaces}{lines}")

