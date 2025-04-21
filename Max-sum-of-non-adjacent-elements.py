# Using recursion: FInding the max sum of non-adjacent elements
def maxSum_recursion(nums, n):
    # Base case: if the list is empty
    if n < 0:
        return 0
    # Base case:  if the list has only one element
    if n == 0:
        return nums[0]
    
    include = maxSum_recursion(nums, n - 2) + nums[n]
    exclude = maxSum_recursion(nums, n - 1) + 0

    return max(include, exclude)


# Using Top-Down Dynamic Programming (Memoization)
def maxSum_memoization(nums, n, memo={}):
    # Base case: if the list is empty
    if n < 0:
        return 0
    # Base case:  if the list has only one element
    if n == 0:
        return nums[0]

    # Check if the result already computed or not 
    if n in memo:
        return memo[n]
    
    include = maxSum_memoization(nums, n - 2, memo) + nums[n]
    exclude = maxSum_memoization(nums, n - 1, memo) + 0
    memo[n] = max(include, exclude)
    return memo[n]


# Using Bottom-Up Dynamic Programming (Tabulation)
def maxSum_tabulation(nums, n):
    # Initialize a dp array
    dp = [0] * n

    # Base cases
    dp[0] = nums[0]

    # Fill the dp array iteratively
    for i in range(1, n):
        include = dp[i - 2] + nums[i]
        exclude = dp[i - 1] + 0
        dp[i] = max(include, exclude)

    return dp[n - 1]


# Space optimized solution
def maxSum_space_optimized(nums, n):
    # Initialize two variables to store base case values
    prev2, prev1 = 0, nums[0]

    # Fill the dp array iteratively
    for i in range(1, n):
        include = prev2 + nums[i]
        exclude = prev1 + 0
        ans = max(include, exclude)

        prev2, prev1 = prev1, ans

    return prev1



"""
Question: Given the list of integers, find the maximum sun of non-adjacent elements.
"""


if __name__ == '__main__':
    nums = [9, 9, 8, 2]
    n = len(nums)

    # Test the recursive function
    result = maxSum_recursion(nums, n - 1) # start from the last index
    print(f"Maximum sum is {result}\n")

    # Test the Top-down DP(Memoization) function
    result = maxSum_memoization(nums, n - 1) # start from the last index
    print(f"Maximum sum is {result}\n")

    # Test the Bottom-up DP(Tabulation) function
    result = maxSum_tabulation(nums, n)
    print(f"Maximum sum is {result}\n")

    # Test the space optimized function
    result = maxSum_space_optimized(nums, n)
    print(f"Maximum sum is {result}\n")