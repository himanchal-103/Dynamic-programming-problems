# Using recursion
def findWays_recursion(nums, tar):
    # Base case: if tar < 0
    if tar < 0:
        return 0
    
    # Base case: if tar == 0
    if tar == 0:
        return 1
    
    ans = 0
    for i in range(len(nums)):
        ans += findWays_recursion(nums, tar - nums[i])
    
    return ans


# Using Top-Down Dynamic Programming (Memoization)
def findWays_memoization(nums, tar, dp):
    # Base case: if tar < 0
    if tar < 0:
        return 0
    
    # Base case: if tar == 0
    if tar == 0:
        return 1
    
    # Check if the result already computed or not
    if dp[tar] != -1:
        return dp[tar]
    
    ans = 0
    for i in range(len(nums)):
        ans += findWays_memoization(nums, tar - nums[i], dp)
    dp[tar] = ans

    return dp[tar]


# Using Bottom-Up Dynamic Programming (Tabulation)
def findWays_tabulation(nums, tar):
    dp = [0] * (tar + 1)

    # Base case: if tar < 0 or tar == 0
    dp[0] = 1

    # traversing from 1 to tar
    for i in range(1, tar + 1):
        # traversing on nums
        for j in range(len(nums)):
            if (i - nums[j]) >= 0:
                dp[i] += dp[i - nums[j]]
    
    return dp[tar]


"""
Problem statement:
You are given an array of distinct integers.
You have to tell how many different ways of selecting the elements from the arrayare there such that the sum of chosen elements is equal to the target.

"""

if __name__ == '__main__':
    tar = 5
    array = [1, 2, 5] # output: 9

    # Test the recursive function
    print(f"Number of ways: {findWays_recursion(array, tar)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [-1] * (tar + 1)
    print(f"Number of ways: {findWays_memoization(array, tar, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Number of ways: {findWays_tabulation(array, tar)}\n")
