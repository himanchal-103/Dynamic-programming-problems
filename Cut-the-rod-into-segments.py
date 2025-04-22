# Using recursion
def cutSegment_recursion(n, x, y, z):
    # Base case: if length of rod is 0
    if n == 0:
        return 0
    
    # Base case: if length of rod is negative
    if n < 0:
        return float('-inf')
    
    # Recursive call for each segment
    a = cutSegment_recursion(n - x, x, y, z) + 1
    b = cutSegment_recursion(n - y, x, y, z) + 1
    c = cutSegment_recursion(n - z, x, y, z) + 1

    return max(a, b, c)


# Using Top-Down Dynamic Programming (Memoization)
def cutSegment_memoization(n, x, y, z, memo={}):
    # Base case: if length of rod is 0
    if n == 0:
        return 0
    
    # Base case: if length of rod is negative
    if n < 0:
        return float('-inf')
    
    # Check if the result already computed or not 
    if n in memo:
        return memo[n]
    
    # Recursive call for each segment
    a = cutSegment_memoization(n - x, x, y, z, memo) + 1
    c = cutSegment_memoization(n - z, x, y, z, memo) + 1
    b = cutSegment_memoization(n - y, x, y, z, memo) + 1

    memo[n] = max(a, b, c)
    return memo[n]


# Using Bottom-Up Dynamic Programming (Tabulation)
def cutSegment_tabulation(n, x, y, z):
    dp = [float('-inf')] * (n + 1)

    # Base case: if length of rod is 0
    dp[0] = 0

    # Fill the dp array iteratively
    for i in range(1, n + 1):
        if i - x >= 0:
            dp[i] = max(dp[i], dp[i - x] + 1)
        if i - y >= 0:
            dp[i] = max(dp[i], dp[i - y] + 1)
        if i - z >= 0:
            dp[i] = max(dp[i], dp[i - z] + 1)
    
    if dp[n] < 0:
        return 0
    else:
        return dp[n]



"""
Problem Statement: 
You are given a rod of length 'N'. You need to determine the maximum number of segments you can make form this rod. 
Provided that each segment should be of length x, y, z.
"""

if __name__ == '__main__':
    # n, x, y, z = 7, 5, 2, 2
    n, x, y, z = 8, 3, 3, 3

    # Test the recursive function
    ans = cutSegment_recursion(n, x, y, z)
    if ans <= 0:
        print("Not possible to cut the rod into segments.\n")
    else:
        print(f"Maximum number of segments are {ans}\n")


    # Test the Top-down DP(Memoization) function
    ans = cutSegment_memoization(n, x, y, z)
    if ans <= 0:
        print("Not possible to cut the rod into segments.\n")
    else:
        print(f"Maximum number of segments are {ans}\n")


    # Test the Bottom-up DP(Tabulation) function
    ans = cutSegment_tabulation(n, x, y, z)
    if ans <= 0:
        print("Not possible to cut the rod into segments.\n")
    else:
        print(f"Maximum number of segments are {ans}\n")