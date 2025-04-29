# Using recursion
def minCost_recursion(n, days, cost, index):
    # Base case: if indexis after travelling day
    if index >= n:
        return 0
    
    # 1 day pass
    option1 = cost[0] + minCost_recursion(n, days, cost, index + 1)

    # 7 day pass
    i = index
    while i < n and days[i] < days[index] + 7:
        i += 1
    option2 = cost[1] + minCost_recursion(n, days, cost, i)

    # 30 days  pass
    i = index
    while i < n and days[i] < days[index] + 30:
        i += 1
    option3 = cost[2] + minCost_recursion(n, days, cost, i)

    return min(option1, option2, option3)


# Using Top-Down Dynamic Programming (Memoization)
def minCost_memoization(n, days, cost, index, memo={}):
    # Base case
    if index >= n:
        return 0
    
    # Check if the result already computed or not 
    if index in memo:
        return memo[index]
    
    # 1 day pass
    opt1 = cost[0] + minCost_memoization(n, days, cost, index + 1, memo)

    # 7 days pass
    i = index
    while i < n and days[i] < days[index] + 7:
        i += 1
    opt2 = cost[1] + minCost_memoization(n, days, cost, i, memo)

    # 30 days pass
    i = index
    while i < n and days[i] < days[index] + 30:
        i += 1
    opt3 = cost[2] + minCost_memoization(n, days, cost, i, memo)

    memo[index] = min(opt1, opt2, opt3)
    return memo[index]
    

# Using Bottom-Up Dynamic Programming (Tabulation)
def minCost_tabulation(n, days, cost):
    # Initialize a dp array
    dp = [float('inf')] * (n + 1)

    # Base cases
    dp[n] = 0

    # Fill the dp array iteratively
    for k in range(n - 1, -1, -1):
        # 1 day pass
        opt1 = cost[0] + dp[k + 1]

        # 7 days pass
        i = k
        while i < n and days[i] < days[k] + 7:
            i += 1
        opt2 = cost[1] + dp[i]

        # 30 days pass
        i = k
        while i < n and days[i] < days[k] + 30:
            i += 1
        opt3 = cost[2] + dp[i]

        dp[k] = min(opt1, opt2, opt3)
    
    return dp[0]



"""
Problem Staement:
You have planned some train traveling one year in advance. 
The days of the year in which you will travel are given as an integer array days. 
Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
1. 1-day pass is sold for costs[0] dollars,
2. 7-day pass is sold for costs[1] dollars, and
3. 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
"""

if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    cost = [2, 7, 15]
    # days = [2, 5]
    # cost = [1, 4, 25]
    n = len(days)

    # Test the recursive function
    print(f"Minimum cost of travelling: {minCost_recursion(n, days, cost, 0)}\n") # 0 represents index

    # Test the Top-down DP(Memoization) function
    print(f"Minimum cost of travelling: {minCost_memoization(n, days, cost, 0)}\n") # 0 represents index

    # Test the Bottom-up DP(Tabulation) function
    print(f"Minimum cost of travelling: {minCost_tabulation(n, days, cost)}\n")

