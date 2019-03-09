change = float(input("How many change you have"))
user_coins = input("Which one coins you want received ")
avaible_coins = list(map(float, user_coins.split()))
avaible_coins.sort(reverse=True)
change_in_coins = []

while (change > min(avaible_coins)):
    for coin in avaible_coins:
        if coin <= change:
            change_in_coins.append(coin)
            change = change - coin
            break

print(f"This is your change in coins: {change_in_coins}")