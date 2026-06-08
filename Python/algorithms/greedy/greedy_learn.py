def coin_change_greedy(coins, amount):
    """
    A greedy algorithm to find the minimum number of coins needed to make a given amount.
    
    Parameters:
    coins (list): A list of coin denominations available.
    amount (int): The total amount of money to make with the coins.
    
    Returns:
    int: The minimum number of coins needed to make the amount, or -1 if it is not possible.
    
    Example:
    >>> coin_change_greedy([1, 5, 10, 25], 63)
    6
    """
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

# Example usage
if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = 63
    print(f"Minimum coins needed: {coin_change_greedy(coins, amount)}")