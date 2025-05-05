# Using recursion
def maxSatisfaction_recursion(satisfaction, index, time):
    # Base case
    if index == len(satisfaction):
        return 0
    
    include = (satisfaction[index] * (time + 1)) + maxSatisfaction_recursion(satisfaction, index + 1, time + 1)
    exclude = maxSatisfaction_recursion(satisfaction, index + 1, time)

    return max(include, exclude)


# Using Top-Down Dynamic Programming (Memoization)
def maxSatisfaction_memoization(satisfaction, index, time, dp):
    # Base case
    if index == len(satisfaction):
        return 0
    
    # Check if the result already computed or not 
    if dp[index][time] != -1:
        return dp[index][time]
    
    include = (satisfaction[index] * (time + 1)) + maxSatisfaction_memoization(satisfaction, index + 1, time + 1, dp)
    exclude = maxSatisfaction_memoization(satisfaction, index + 1, time, dp)

    dp[index][time] = max(include, exclude)
    return dp[index][time]


# Using Bottom-Up Dynamic Programming (Tabulation)
def maxSatisfaction_tabulation(satisfaction):
    n = len(satisfaction)

    # Initialize a dp array
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    # Base case already handles as array is initialized with 0

    for index in range(n - 1, -1, -1):
        for time in range(index, -1, -1):
            include = (satisfaction[index] * (time + 1)) + dp[index + 1][time + 1]
            exclude = dp[index + 1][time]

            dp[index][time] = max(include, exclude)
    
    return dp[0][0]


# Space optimized solution
def maxSatisfaction_space_optimized(satisfaction):
    n = len(satisfaction)

    # Initialize a dp array
    curr = [0] * (n + 1)
    nxt = [0] * (n + 1)

    for index in range(n - 1, -1, -1):
        for time in range(n):
            include = (satisfaction[index] * (time + 1)) + nxt[time + 1]
            exclude = nxt[time]

            curr[time] = max(include, exclude)
        nxt = curr
    
    return nxt[0]



"""
Problem Statement: Leetcode 1402

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
Return the maximum sum of like-time coefficient that the chef can obtain after preparing some amount of dishes.
Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example:
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

"""


if __name__ == '__main__':
    # satisfaction = [-1,-8,0,5,-9] # output: 14
    satisfaction = [-1,-4,-5] # output: 0

    # Sort in ascending order
    satisfaction = sorted(satisfaction)
    
    # Test the recursive function
    print(f"Result: {maxSatisfaction_recursion(satisfaction, 0, 0)}\n")

    # Test the Top-down DP(Memoization) function
    n = len(satisfaction)
    dp = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]
    print(f"Result: {maxSatisfaction_memoization(satisfaction, 0, 0, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Result: {maxSatisfaction_tabulation(satisfaction)}\n")

    # Test the space optimized function
    print(f"Result: {maxSatisfaction_space_optimized(satisfaction)}\n")

