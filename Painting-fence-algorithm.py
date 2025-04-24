# Using recursion
def paint_recursion(n, k):
    # Base case: if n == 1
    if n == 1:
        return k
    
    # Base case: if n == 2
    if n == 2:
        return k + (k * (k - 1))
    
    # Call function recursively
    ans = (k - 1) * (paint_recursion(n - 2, k) + paint_recursion(n - 1, k))
    return ans


# Using Top-Down Dynamic Programming (Memoization)
def paint_memoization(n, k, memo={}):
    # Base case: if n == 1 or n == 2
    if n == 1:
        return k
    if n == 2:
        return k + (k * (k - 1))
    
    # Check if the result already computed or not 
    if n in memo:
        return memo[n]
    
    memo[n] = (k - 1) * (paint_memoization(n - 2, k, memo) + paint_memoization(n - 1, k, memo))
    return memo[n]


# Using Bottom-Up Dynamic Programming (Tabulation)
def paint_tabulation(n, k):
    # Initialize a dp array
    dp = [0] * (n + 1)

    # Base cases
    dp[1], dp[2] = k, k + (k * (k - 1))

    # Fill the dp array iteratively
    for i in range(3, n + 1):
        dp[i] = (k - 1) * (dp[i - 2] + dp[i - 1])

    return dp[n]


# Space optimized solution
def paint_space_optimized(n, k):
    # Initialize two variables to store base case values
    prev2, prev1 = k, k + (k * (k - 1)) 

    for _ in range(3, n + 1):
        prev2, prev1 = prev1, (k - 1) * (prev2 + prev1)

    return prev1



"""
Problem Statement:
Ninja has given a fence, and he gave a task to paint this fence.
The fence has 'N' posts and Ninja has 'K' colors. Ninja wants to paint the fence so that not more than two adjacent posts have same color.
Tasks is to find the number of ways that Ninja can paint the fence
"""
if __name__ == '__main__':
    n, k = 3, 2 # output : 6
    
    # Test the recursive function
    print(f"Total number of ways: {paint_recursion(n, k)}\n")

    # Test the Top-down DP(Memoization) function
    print(f"Total number of ways: {paint_memoization(n, k)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Total number of ways: {paint_tabulation(n, k)}\n")

    # Test the space optimized function
    print(f"Total number of ways: {paint_space_optimized(n, k)}\n")