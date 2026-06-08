# File: coin_changing.py
# COIN CHANGING PROBLEMS.

import sys
sys.setrecursionlimit(10000)

# Some coin systems:

lecture_coins = [1,5,7]    

sterling_coins = [1,2,5,10,20,50,100,200]


# Problem (1): Minimum number of coins (as in Lecture 18).

c_list = lecture_coins  # global variable, can set as desired


# Plain recursive implementation.
# fewest_coins should be implemented recursively, returning just smallest number of coins.

def fewest_coins(v):
    if v == 0:
        return 0
    # Init 
    if v < 0:
        return float('inf')

    # Recursive case: Try each coin and take the minimum result
    min_coins = float('inf')
    for c in c_list:
            min_coins = min(min_coins, fewest_coins(v - c) + 1)

    return min_coins

# slightly different method which returns a list of actual coins (which constitute a 
# minimum-sized solution).

def fewest_coins_list(v):
    if v == 0:
        return []
    
    # Recursive case: Try each coin and get the optimal list
    min_coins = float('inf')
    best_coins = []
    for coin in c_list:
        if coin <= v:
            remaining_coins = fewest_coins_list(v - coin)
            if len(remaining_coins) + 1 < min_coins:
                min_coins = len(remaining_coins) + 1
                best_coins = remaining_coins + [coin]
    return best_coins


# Memoization operation, exactly as in our lecture:

def memoize(f):
    memo = {}
    def check(v):
        if v not in memo:
            memo[v] = f(v)
        return memo[v]
    return check

# memoize : (int->int) -> (int->int)
# f : int->int,  check : int->int

# To get the optimization of the recursion:

# fewest_coins = memoize(fewest_coins)
# fewest_coins_list = memoize(fewest_coins_list)

# NB. Can't change c_list after doing this!
# We would need to reload the file within the Python interpreter to use with new c_list.

# You should also implement and experiment with a dynamic programming solution,
# as given towards the end of slide-set 18.


def fewest_coins_dp(v):
    dp = [float('inf')] * (v + 1)
    dp[0] = 0
    for i in range(1, v + 1):
        for coin in c_list:
            if coin <= i:
                """
                dp[i - coin] + 1 is the heart of dynamic programming
                """
                dp[i] = min(dp[i], dp[i - coin] + 1) # dp[i - coin] + 1 is a cumulative process

def fewest_coins_list_dp(v):
    dp = [float('inf')] * (v + 1)
    dp[0] = 0
    coin_used = [0] * (v + 1) # to track what coin is used

    for i in range(1, v + 1):
        for coin in c_list:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Reconstruct the list of coins
    coins = []
    while v > 0:
        coins.append(coin_used[v])
        v -= coin_used[v]

    return coins

if __name__ == "__main__":
    print(fewest_coins_list(10))