# Using recursion
def isPossible_recursion(index, arr, N, target):
    # Base case
    if (index >= N) or (target < 0): 
        return 0
    
    if target == 0:
        return 1
    
    include = isPossible_recursion(index + 1, arr, N, target - arr[index])
    exclude = isPossible_recursion(index + 1, arr, N, target)

    return include or exclude


# Using Top-Down Dynamic Programming (Memoization)
def isPossible_memoization(index, arr, N, target, dp):
    # Base case
    if (index >= N) or (target < 0): 
        return 0
    
    if target == 0:
        return 1
    
    # Check if the result already computed or not 
    if dp[index][target] != -1:
        return dp[index][target]

    include = isPossible_memoization(index + 1, arr, N, target - arr[index], dp)
    exclude = isPossible_memoization(index + 1, arr, N, target, dp)

    dp[index][target] = include or exclude
    return dp[index][target]


# Using Bottom-Up Dynamic Programming (Tabulation)
def isPossible_tabulation(arr, N, total):
    # Initialize an dp array
    dp = [[0 for _ in range(total + 1)] for _ in range(N + 1)]

    # Base case
    for i in range(N + 1):
        dp[i][0] = 1

    for index in range(N - 1, -1, -1):
        for target in range(0, (total // 2) + 1):
            include = 0
            if (target - arr[index]) >= 0:
                include = dp[index + 1][target - arr[index]]
            exclude = dp[index + 1][target]

            dp[index][target] = include or exclude
    
    return dp[0][total // 2]


# Space optimized solution
def isPossible_space_optimized(arr, N, total):
    # Initialize an array
    curr = [0] * (total + 1)
    nxt = [0] * (total + 1)

    # Base cases
    curr[0], nxt[0] = 1, 1

    for index in range(N - 1, -1, -1):
        for target in range(0, (total // 2) + 1):
            include = 0
            if (target - arr[index]) >= 0:
                include = nxt[target - arr[index]]
            exclude = nxt[target]

            curr[target] = include or exclude
        
        nxt = curr
    
    return nxt[total // 2]



"""
Problem Statement:

Given an array arr[] of size 'N'.
Check if it can be partitioned into two parts, such that the sum of elements in both parts is the same.

if partition is possible return 1 else return 0

Example:
Input: N = 4
arr = [1, 5, 11, 5]
output: YES
explanation: part1 will be [1,5,5] and part2 will be [11]

"""


if __name__ == '__main__':
    arr = [1, 5, 11, 5] # output: YES
    # arr = [1, 5, 3] # output: NO (odd sum case)
    # arr = [3, 4, 3] # output: NO
    N = len(arr)

    # if the sum is odd, then partition is not possible, and there is no need to call functions
    total = sum(arr)

    if total % 2 != 0:
        print(f"Partition is not possible as the array cannot be divided (odd sum case).\n")
    else:
        target = total // 2

        # Test the recursive function
        print(f"Partition is possible or not: {'YES' if isPossible_recursion(0, arr, N, target) else 'NO'}\n") # 0 is the starting index

        # Test the Top-down DP(Memoization) function
        dp = [[-1 for _ in range(target + 2)] for _ in range(N + 1)]
        print(f"Partition is possible or not: {'YES' if isPossible_memoization(0, arr, N, target, dp) else 'NO'}\n") # 0 is the starting index

        # Test the Bottom-up DP(Tabulation) function
        print(f"Partition is possible or not: {'YES' if isPossible_tabulation(arr, N, target) else 'NO'}\n")

        # Test the space optimized function
        print(f"Partition is possible or not: {'YES' if isPossible_space_optimized(arr, N, target) else 'NO'}\n")

