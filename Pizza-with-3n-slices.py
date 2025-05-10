# Using recursion
def maxSlices_recursion(index, endindex, slices, n):
    # Base case
    if  (n == 0) or (index > endindex):
        return 0
    
    include = slices[index] + maxSlices_recursion(index + 2, endindex, slices, n - 1)
    exclude = maxSlices_recursion(index + 1, endindex, slices, n)

    return max(include, exclude)


# Using Top-Down Dynamic Programming (Memoization)
def maxSlices_memoization(index, endindex, slices, n, dp):
    # Base case
    if  (n == 0) or (index > endindex):
        return 0
    
    # Check if the result already computed or not 
    if dp[index][n] != -1:
        return dp[index][n]
    
    include = slices[index] + maxSlices_memoization(index + 2, endindex, slices, n - 1, dp)
    exclude = maxSlices_memoization(index + 1, endindex, slices, n, dp)

    dp[index][n] = max(include, exclude)
    return dp[index][n]


# Using Bottom-Up Dynamic Programming (Tabulation)
def maxSlices_tabulation(slices):
    # Initialize a dp array
    k = len(slices)
    dp1 = [[0 for _ in range(k + 2)] for _ in range(k + 2)]
    dp2 = [[0 for _ in range(k + 2)] for _ in range(k + 2)]

    # Base case already handles as array is initialized with 0

    for index in range(k - 2, -1, -1):
        for n in range(1, k//3 + 1):
            include = slices[index] + dp1[index + 2][n - 1]
            exclude = dp1[index + 1][n]
            dp1[index][n] = max(include, exclude)
    case1 = dp1[0][k//3]
    
    for index in range(k - 1, 0, -1):
        for n in range(1, k//3 + 1):
            include = slices[index] + dp2[index + 2][n - 1]
            exclude = dp2[index + 1][n]
            dp2[index][n] = max(include, exclude)
    case2 = dp2[1][k//3]

    return max(case1, case2)


# Space optimized solution
def maxSlices_space_optimized(slices):
    # Initialize a array
    k = len(slices)

    prev1 = [0] * (k + 2)
    curr1 = [0] * (k + 2)
    nxt1 = [0] * (k + 2)
    
    prev2 = [0] * (k + 2)
    curr2 = [0] * (k + 2)
    nxt2 = [0] * (k + 2)

    # Base case already handles as array is initialized with 0

    for index in range(k - 2, -1, -1):
        for n in range(1, k//3 + 1):
            include = slices[index] + nxt1[n - 1]
            exclude = curr1[n]
            prev1[n] = max(include, exclude)
        nxt1, curr1, prev1 = curr1, prev1, [0] * (k + 2)
    case1 = curr1[k//3]
    
    for index in range(k - 1, 0, -1):
        for n in range(1, k//3 + 1):
            include = slices[index] + nxt2[n - 1]
            exclude = curr2[n]
            prev2[n] = max(include, exclude)
        nxt2, curr2, prev2 = curr2, prev2, [0] * (k + 2)
    case2 = curr2[k//3]

    return max(case1, case2)


"""
Problem statement: Leetcode problem no. 1388

There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:
You will pick any pizza slice.
Your friend Alice will pick the next slice in the anti-clockwise direction of your pick.
Your friend Bob will pick the next slice in the clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Given an integer array slices that represent the sizes of the pizza slices in a clockwise direction, return the maximum possible sum of slice sizes that you can pick.

Example:
Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. 
Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.

"""


if __name__ == '__main__':
    # slices = [1, 2, 3, 4, 5, 6] # output: 10
    slices = [8, 9, 8, 6, 1, 1] # output: 16

    k = len(slices)

    # Test the recursive function
    case1 = maxSlices_recursion(0, k - 2, slices, k // 3)
    case2 = maxSlices_recursion(1, k - 1, slices, k // 3)

    print(f"Maximum possible sum: {max(case1, case2)}\n")

    # Test the Top-down DP(Memoization) function
    dp1 = [[-1 for _ in range(k)] for _ in range(k)]
    case1 = maxSlices_memoization(0, k - 2, slices, k // 3, dp1)

    dp2 = [[-1 for _ in range(k)] for _ in range(k)]
    case2 = maxSlices_memoization(1, k - 1, slices, k // 3, dp2)

    print(f"Maximum possible sum: {max(case1, case2)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Maximum possible sum: {maxSlices_tabulation(slices)}\n")

    # Test the space optimized function
    print(f"Maximum possible sum: {maxSlices_space_optimized(slices)}\n")
