#  Using Recursion: Finding minimum number of coins
def minCoins_recursion(coins, total):
    # Base case: if the total amount is 0, return 0
    if total == 0:
        return 0
    
    # Initialize the minimum number of coins to a large value
    min_coins = float('inf')

    # Iterate through each coin denomination
    for coin in coins:
        if coin <= total:
            res = minCoins_recursion(coins, total - coin)
            if res != -1:
                min_coins = min(min_coins, res + 1)
    
    return min_coins if min_coins != float('inf') else -1


# Using Top-Down Dynamic Programming (Memoization)
def minCoins_memoization(coins, total, memo={}):
    # Base case: if the total amount is 0, return 0
    if total == 0:
        return 0
    
    # Check if the result already computed or not
    if total in memo:
        return memo[total]
    
    # Initialize the minimum number of coins to a large value
    min_coins = float('inf')

    # Iterate through each denomination
    for coin in coins:
        if coin <= total:
            res = minCoins_memoization(coins, total - coin, memo)
            if res != -1:
                min_coins = min(min_coins, res + 1)  # store the result

    memo[total] = min_coins if min_coins != float('inf') else -1
    return memo[total]


# Using Bottom-Up Dynamic Programming (Tabulation)
def minCoins_tabulation(coins, total):
    # Initialize a dp array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)

    # Base Case: 0 coins are needed to make the amount 0
    dp[0] = 0

    # Fill the dp array iteratively for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1) # Store the minimum number of coins needed to make the amount
                
    # Return the minimum number of coins needed to make the total amount
    return dp[total] if dp[total] != float('inf') else -1



"""
Question: You are given 'N' distinct coins of denominations 'a1', 'a2', 'a3', ..., 'aN' and a total amount 'T'.
You need to find the minimum number of coins required to make the total amount 'T'.
"""

if __name__ == '__main__':
    coins = [2, 5] # Coin denominations
    total = 11 # Total amount

    # Test the recursive function
    result = minCoins_recursion(coins, total)
    if result != -1:
        print(f"Minimum number of coins required to make the total amount {total}: {result}\n")
    else:
        print(f"It's not possible to make the total amount {total} with the given coin denominations.\n")

    # Test the Top-down DP(Memoization) function
    result = minCoins_memoization(coins, total)
    if result != -1:
        print(f"Minimum number of coins required to make the total amount {total}: {result}\n")
    else:
        print(f"It's not possible to make the total amount {total} with the given coin denominations.\n")

    # Test the Bottom-up DP(Tabulation) function
    result = minCoins_tabulation(coins, total)
    if result != -1:
        print(f"Minimum number of coins required to make the total amount {total}: {result}\n")
    else:
        print(f"It's not possible to make the total amount {total} with the given coin denominations.\n")
