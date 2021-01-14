# Author: Paul Quaife
# Date: 1/12/2020
# Description: Gives change for less than a dollar in highest amount.

print("Please enter an amount in cents less than a dollar.")
coins = int(input())
print("Your change will be:")
print("Q:", coins // 25)
coins = coins % 25
print("D:", coins // 10)
coins = coins % 10
print("N:", coins // 5)
coins = coins % 5
print("P:", coins)
