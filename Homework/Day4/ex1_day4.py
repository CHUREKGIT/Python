# This program print the change from available coins:
# available_coins: 5,2,1,0.5, 0.2, 0.1

change = float(input("How many change you have"))
available_coins = [0.05, 5, 2, 1, 0.5, 0.2, 0.1]
available_coins.sort(reverse=True)
change_in_coins = []

while (change > 0.1):
     for coin in available_coins:
        if coin <= change:
            change_in_coins.append(coin) #Adding coin to the list for client
            change = change - coin
            break #without break it will not start from begging

ask = input("Can I Keep the change?")

if ask.lower() == 'no':
    change_in_coins.append(0.1)


print(f"This is ypu change in coins: {change_in_coins}")