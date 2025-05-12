# Using recursion
def noOfWays_recursion(dice, faces, target):
    # Base case
    if (target < 0) or (dice == 0 and target != 0) or (dice != 0 and target == 0):
        return 0
    
    # Base case
    if target == 0 and dice == 0:
        return 1
    
    ans = 0
    for i in range(1, faces + 1):
        ans += noOfWays_recursion(dice - 1, faces, target - i)

    return ans    


# Using Top-Down Dynamic Programming (Memoization)
def noOfWays_memoization(dice, faces, target, dp):
    # Base case
    if (target < 0) or (dice == 0 and target != 0) or (dice != 0 and target == 0):
        return 0
    
    # Base case
    if target == 0 and dice == 0:
        return 1
    
    # Check if the result already computed or not 
    if dp[dice][target] != -1:
        return dp[dice][target]

    ans = 0
    for i in range(1, faces + 1):
        ans += noOfWays_memoization(dice - 1, faces, target - i, dp)

    dp[dice][target] = ans 
    return dp[dice][target]


# Using Bottom-Up Dynamic Programming (Tabulation)
def noOfWays_tabulation(d, f, t):
    # Initialize a dp array
    dp = [[0 for _ in range(t + 2)] for _ in range(d + 1)]

    # Base case
    dp[0][0] = 1

    for dice in range(1, d + 1):
        for target in range(1, t + 1):
            ans = 0
            for i in range(1, f + 1):
                if target - i >= 0:
                    ans += dp[dice - 1][target - i]

            dp[dice][target] = ans
    
    return dp[d][t]


# Space optimized solution
def noOfWays_space_optimized(d, f, t):
    # Initialize an array
    prev = [0] * (t + 1)
    curr = [0] * (t + 1)

    # Base case
    prev[0] = 1

    for dice in range(1, d + 1):
        curr = [0] * (t + 1) # Reset curr at each dice level
        for target in range(1, t + 1):
            ans = 0
            for i in range(1, f + 1):
                if target - i >= 0:
                    ans += prev[target - i]

            curr[target] = ans
        prev = curr
    
    return prev[t]



"""
Problem Statement:

Given 'N' dice each with 'M' faces, numbered from 1 to M. Find the number of ways to get sum 'X'.
X is the summation of values on each faces when all the dice are thrown.

Example:
M = 6, N = 3, X = 12
output: 25
explanation: There are 25 total ways to get the sum 12 using 3 dices with faces from 1 to 6.

"""


if __name__ == '__main__':
    m = 6 # number of faces
    n = 3 # number of dice
    x = 12 # target sum # output: 25

    # Test the recursive function
    print(f"Number of ways: {noOfWays_recursion(n, m, x)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(x + 2)] for _ in range(n + 1)] # size of the colunms should be x + 1
    print(f"Number of ways: {noOfWays_memoization(n, m, x, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Number of ways: {noOfWays_tabulation(n, m, x)}\n")

    # Test the space optimized function
    print(f"Number of ways: {noOfWays_space_optimized(n, m, x)}\n")
