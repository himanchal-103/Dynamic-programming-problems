# Using recursion
def longestAP_recursion(index, diff, A):
    # Backword check
    if index < 0:
        return 0
    
    ans = 0
    for j in range(index - 1, -1, -1):
        if A[index] - A[j] == diff:
            ans = max(ans, 1 + longestAP_recursion(j, diff, A))
    
    return ans


# Using Top-Down Dynamic Programming (Memoization)
def longestAP_memoization(index, diff, A, dp):
    if index < 0:
        return 0
    
    # Check if the result already computed or not 
    if diff in dp[index]:
        return dp[index][diff]
    
    ans = 0
    for j in range(index - 1, -1, -1):
        if A[index] - A[j] == diff:
            ans = max(ans, 1 + longestAP_memoization(j, diff, A, dp))
    
    dp[index][diff] = ans
    return dp[index][diff]



"""
Problem Statement:

Given an arraycalled A[] of sorted integers having no duplicates.
Find the length of longest arithmetic progression in it.

Example:
N = 6
A = [1, 7, 10, 13, 14, 19]
output: 4
explanation: The longest arithmetic progression is [1, 7, 13, 19]

"""


if __name__ == '__main__':
    A = [1, 7, 10, 13, 14, 19] # output: 4
    N = len(A)

    # If length of input array is less than or equal to 2 then it is the final output
    if N <= 2:
        print(f"Longest arithmetic progression is: {N}\n")
    else:
        # Test the recursive function
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                ans = max(ans, 2 + longestAP_recursion(i, A[j] - A[i], A))
                
        print(f"Longest arithmetic progression is: {ans}\n")

        # Test the Top-down DP(Memoization) function
        ans = 0
        dp = [{} for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                ans = max(ans, 2 + longestAP_memoization(i, A[j] - A[i], A, dp))
                
        print(f"Longest arithmetic progression is: {ans}\n")
