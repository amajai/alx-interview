#!/usr/bin/python3
"""
makeChange module
"""


def makeChange(coins, amount):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
