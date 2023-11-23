#!/usr/bin/python3

'''
Module to calculate the least number of coins required to meet total
'''


def makeChange(coins, total):
    '''
    Determine the fewest number of coins required to 
    achieve the passed total
    '''
    if total < 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
    