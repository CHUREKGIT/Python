card0 = input("Give me first cart")
card0 = input("Give me second cart")

points_min = 0
points_max = 0


if card0 in "23456789":
    points_min = points_min + int(card0)
    points_max = points_max + int(card0)
elif card0 in "JQK":
    points_min = points_min + 10
    points_max = points_max + 10
elif card0 in "A":
    points_min = points_min + 1
    points_max = points_max + 11

if card1 in "23456789":
    points_min = points_min + int(card1)
    points_max = points_max + int(card1)
elif card1 in "JQK":
    points_min = points_min + 10
    points_max = points_max + 10
elif card1 in "A":
    points_min = points_min + 1
    points_max = points_max + 11

#Check if is win or you need another cart

if points_min == 21 or points_max == 21:
    print("stop, you won!")
elif points_min >18 or points_max > 18:
    print("stop, you have at least 19 points")
else:
    print("You can take another cart")