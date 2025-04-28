# Using recursion
def minSquare_recursion(n):
    # Base case: if n == 0
    if n == 0:
        return 0
    
    i, ans = 1, n
    while i**2 <= n:
        ans = min(ans, 1 + minSquare_recursion(n - i**2))
        i += 1

    return ans


# Using Top-Down Dynamic Programming (Memoization)
def minSquare_memoization(n, memo={}):
    # Base case
    if n == 0:
        return 0
    
    # Check if the result already computed or not
    if n in memo:
        return memo[n]
    
    i, ans = 1, n
    while i**2 <= n:
        ans = min(ans, 1 + minSquare_memoization(n - i**2, memo))
        i += 1
    
    memo[n] = ans
    return memo[n]
    

# Using Bottom-Up Dynamic Programming (Tabulation)
def minSquare_tabulation(n):
    # Initialize a dp array
    dp = [float('inf')] * (n + 1)

    # Base case
    dp[0] = 0

    # Fill the dp array iteratively
    for i in range(1, n + 1):
        j = 0
        while j**2 <= n:
            if i - j**2 >= 0:
                dp[i] = min(dp[i], 1 + dp[i - j**2])
            j += 1

    
    return dp[n]



"""
Problem statement:
Given the number 'N'. FInd the minimum number of squares of any number that sums to N.
For example: 
If N = 100. N can be expressed as (10 * 10) and also as (5*5 + 5*5 + 5*5 + 5*5) but the output will be 1 as minimum number of square is 1 that is 10
"""

if __name__ == '__main__':
    # N = 100 # ouput: 1
    N = 6 # output: 3

    # Test the recursive function
    print(f"Output: {minSquare_recursion(N)}\n")

    # Test the Top-down DP(Memoization) function
    print(f"Output: {minSquare_memoization(N)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Output: {minSquare_tabulation(N)}\n")
