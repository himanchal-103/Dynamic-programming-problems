# Using recursion
def cnt_recursion(n):
    # Base case: if n == 1 or n == 2
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Call function recursively
    ans = (n - 1) * (cnt_recursion(n - 1) + cnt_recursion(n - 2))
    return ans
    

# Using Top-Down Dynamic Programming (Memoization)
def cnt_memoization(n, memo={}):
    # Base case: if n == 1 or n == 2
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Check if the result already computed or not 
    if n in memo:
        return memo[n]
    
    memo[n] = (n - 1) * (cnt_memoization(n - 1, memo) + cnt_memoization(n - 2, memo))
    return memo[n]


# Using Bottom-Up Dynamic Programming (Tabulation)
def cnt_tabulation(n):
    # Initialize a dp array
    dp = [0] * (n + 1)

    # Base cases
    dp[1], dp[2] = 0, 1

    # Fill the dp array iteratively
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])

    return dp[n]


# Space optimized solution
def cnt_space_optimized(n):
    # Initialize two variables to store base case values
    prev2, prev1 = 0, 1

    # Fill the dp array iteratively
    for i in range(3, n + 1):
        prev2, prev1 = prev1, (i - 1) * (prev1 + prev2)

    return prev1


"""
Problem Statement:
A derangement is a permutation of 'N' elements such that no elements appears in the original position.
Given a number 'N', find the total number of derangements possible of the set of 'N' elements.
"""
if __name__ == '__main__':
    n = 4

    # Test the recursive function
    print(f"Total number of ways: {cnt_recursion(n)}\n")

    # Test the Top-down DP(Memoization) function
    print(f"Total number of ways: {cnt_memoization(n)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Total number of ways: {cnt_tabulation(n)}\n")

    # Test the space optimized function
    print(f"Total number of ways: {cnt_space_optimized(n)}\n")