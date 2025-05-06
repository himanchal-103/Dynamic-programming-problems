# Using recursion
def longest_recursion(n, a, curr, prev):
    # Base case: if traversing is complete that is curr == n
    if curr == n:
        return 0
    
    # include element
    include = 0
    if (prev == -1) or (a[curr] > a[prev]):
        include = 1 + longest_recursion(n, a, curr + 1, curr)

    # exclude element
    exclude = longest_recursion(n, a, curr + 1, prev)

    return max(include, exclude)


# Using Top-Down Dynamic Programming (Memoization)
def longest_memoization(n, a, curr, prev, dp):
    # Base case: if traversing is complete that is curr == n
    if curr == n:
        return 0
    
    # Check if the result already computed or not 
    if dp[curr][prev + 1] != -1:
        return dp[curr][prev + 1]
    
    # include element
    include = 0
    if (prev == -1) or (a[curr] > a[prev]):
        include = 1 + longest_memoization(n, a, curr + 1, curr, dp)

    # exclude element
    exclude = longest_memoization(n, a, curr + 1, prev, dp)

    dp[curr][prev + 1] = max(include, exclude)
    return dp[curr][prev + 1]


# Using Bottom-Up Dynamic Programming (Tabulation)
def longest_tabulation(n , a):
    # Initialize a dp array
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 1)]

    # Base case already handles as array is initialized with 0

    for curr in range(n - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            # include element
            include = 0
            if (prev == -1) or (a[curr] > a[prev]):
                include = 1 + dp[curr + 1][curr + 1]

            # exclude element
            exclude = dp[curr + 1][prev + 1]

            dp[curr][prev + 1] = max(include, exclude)
    
    return dp[0][0]


# Space optimized solution
def longest_space_optimized(n, a):
    # Initialize a dp array
    currRow = [0] * (n + 1)
    nextRow = [0] * (n + 1)

    for curr in range(n - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            # include element
            include = 0
            if (prev == -1) or (a[curr] > a[prev]):
                include = 1 + nextRow[curr + 1]

            # exclude element
            exclude = nextRow[prev + 1]

            currRow[prev + 1] = max(include, exclude)
        nextRow = currRow
    
    return nextRow[0]



"""
Problem statement:

Given the integer array, find the lenght of longest increasing subsequence from the given array.

For example:
n = 6
arr = [5, 8, 3, 7, 9, 1]
output: 3 as longest sequence would be [5, 7, 9] of length 3
"""

if __name__ == '__main__':
    n = 6
    arr = [5, 8, 3, 7, 9, 1]

    # Test the recursive function
    print(f"Length of longest subsequence: {longest_recursion(n, arr, 0, -1)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(n + 2)] for _ in range(n + 1)]
    print(f"Length of longest subsequence: {longest_memoization(n, arr, 0, -1, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Length of longest subsequence: {longest_tabulation(n, arr)}\n")

    # Test the space optimized function
    print(f"Length of longest subsequence: {longest_space_optimized(n, arr)}\n")

