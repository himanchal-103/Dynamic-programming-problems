# Using Recursion: Finding number ways to climb it
def Solve(nStairs, curStairs):
    # Base case: if the current stair is equal to the number of stairs, return 1
    # This means we have found a valid path to the top
    if curStairs == nStairs:
        return 1
    
    # Base case: if the current stair is greater than the number of stairs, return 0
    # This means we have gone beyond the valid path
    if curStairs > nStairs:
        return 0
    
    return Solve(nStairs, curStairs + 1) + Solve(nStairs, curStairs + 2)


# Using Recursion: Finding minimum cost to climb it
def minCost_recursion(cost, n):
    # Base case: if n is 0, return the cost of the first step
    if n == 0:
        return cost[0]
    
    # Base case: if n is 1, return the cost of the second step
    if n == 1:
        return cost[1]
    
    return cost[n] + min(minCost_recursion(cost, n -1), minCost_recursion(cost, n - 2))


# Using Top-Down Dynamic Programming (Memoization): Finding minimum cost to climb it
def minCost_memoization(cost, n, memo={}):
    # Base case: if n is 0 or 1, return the cost of the step
    if n == 0 or n == 1:
        return cost[n]
    
    # Check if the result for this step is already computed and stored in memo
    if n in memo:
        return memo[n]
    
    # Compute the minimum cost recursively and store it in memo
    memo[n] = cost[n] + min(minCost_memoization(cost, n - 1, memo), minCost_memoization(cost, n - 2, memo))
    return memo[n]


# Using Bottom-Up Dynamic Programming (Tabulation): Finding minimum cost to climb it
def minCost_tabulation(cost, n):
    # Initialize a dp array to store the minimum cost to reach each step
    dp = [-1] * (n + 1)
    
    # Base cases: cost to reach the first and second steps
    dp[0], dp[1] = cost[0], cost[1]

    # Fill the dp array iteratively for each step from 2 to n-1
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    
    # Return the minimum cost to reach the top of the stairs
    # This can be either from the last step or the second last step
    return min(dp[n - 1], dp[n - 2])


# Space optimized solution
def minCost_space_optimized(cost, n):
    # Base case: if n is 0 or 1, return the cost of the step
    if n == 0 or n == 1:
        return cost[n]
    
    # Initialize two variables to store the minimum cost to reach the last two steps
    prev2, prev1 = cost[0], cost[1]

    # Iterate from step 2 to n-1 and update the variables
    for i in range(2, n):
        prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
    
    # Return the minimum cost to reach the top of the stairs
    return min(prev1, prev2)


"""
LeetCode 746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

if __name__ == '__main__':
    # Test the recursive function: Finding number of ways
    nStair = 6 # Number of stairs
    curStair = 0 # Starting from the first stair
    print("Number of ways to reach the top of the stairs: ", Solve(nStair, curStair), '\n')


    cost = [1,100,1,1,1,100,1,1,100,1] # output: 6
    # cost = [10,15,20] # output: 15
    n = len(cost)

    # Test the recursive function: Finding minimum cost
    print("Minimum cost to reach the top of the stairs: ", min(minCost_recursion(cost, n - 1), minCost_recursion(cost, n - 2)), '\n')

    # Test the Top-down DP(Memoization) function
    print("Minimum cost to reach the top of the stairs using memoization: ", min(minCost_memoization(cost, n - 1), minCost_memoization(cost, n - 2)), '\n')

    # Test the Bottom-up DP(Tabulation) function
    print("Minimum cost to reach the top of the stairs using tabulation: ", minCost_tabulation(cost, n), '\n')

    # Test the space optimized function
    print("Minimum cost to reach the top of the stairs using space optimized function: ", minCost_space_optimized(cost, n), '\n')