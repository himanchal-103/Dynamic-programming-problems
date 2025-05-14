# Using recursion
def swap_recursion(nums1, nums2, index, swapped):
    # Base case
    if (index == len(nums1)):
        return 0
    
    ans = float('inf')
    prev1, prev2 = nums1[index - 1], nums2[index - 1]

    # catch
    if swapped:
        prev1, prev2 = prev2, prev1
    
    # no swap case
    if (nums1[index] > prev1) and nums2[index] > prev2:
        ans = swap_recursion(nums1, nums2, index + 1, 0)

    # swap case
    if (nums1[index] > prev2) and (nums2[index] > prev1):
        ans = min(ans, 1 + swap_recursion(nums1, nums2, index + 1, 1))
    
    return ans


# Using Top-Down Dynamic Programming (Memoization)
def swap_memoization(nums1, nums2, index, swapped, dp):
    # Base case
    if (index == len(nums1)):
        return 0
    
    # Check if the result already computed or not 
    if dp[index][swapped] != -1:
        return dp[index][swapped]
    
    ans = float('inf')
    prev1, prev2 = nums1[index - 1], nums2[index - 1]

    # catch
    if swapped:
        prev1, prev2 = prev2, prev1
    
    # no swap case
    if (nums1[index] > prev1) and nums2[index] > prev2:
        ans = swap_memoization(nums1, nums2, index + 1, 0, dp)

    # swap case
    if (nums1[index] > prev2) and (nums2[index] > prev1):
        ans = min(ans, 1 + swap_memoization(nums1, nums2, index + 1, 1, dp))
    
    dp[index][swapped] = ans
    return dp[index][swapped]


# Using Bottom-Up Dynamic Programming (Tabulation)
def swap_tabulation(nums1, nums2):
    # Initialize an dp array
    n = len(nums1)
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]

    # Base case already handles as array is initialized with 0

    for index in range(n - 1, 0, -1):
        for swapped in range(1, -1, -1):
            ans = float('inf')
            prev1, prev2 = nums1[index - 1], nums2[index - 1]

            # catch
            if swapped:
                prev1, prev2 = prev2, prev1
            
            # no swap case
            if (nums1[index] > prev1) and nums2[index] > prev2:
                ans = dp[index + 1][0]

            # swap case
            if (nums1[index] > prev2) and (nums2[index] > prev1):
                ans = min(ans, 1 + dp[index + 1][1])
            
            dp[index][swapped] = ans
    
    return dp[1][0]


# Space optimized solution
def swap_space_optimized(nums1, nums2):
    n = len(nums1)
    swap, noswap = 0, 0

    for index in range(n - 1, 0, -1):
        for swapped in range(1, -1, -1):
            ans = float('inf')
            prev1, prev2 = nums1[index - 1], nums2[index - 1]

            # catch
            if swapped:
                prev1, prev2 = prev2, prev1
            
            # no swap case
            if (nums1[index] > prev1) and nums2[index] > prev2:
                ans = noswap

            # swap case
            if (nums1[index] > prev2) and (nums2[index] > prev1):
                ans = min(ans, 1 + swap)
            
            if swapped:
                currswap = ans
            else:
                currnoswap = ans
        
        swap, noswap = currswap, currnoswap
    
    return min(swap, noswap)


"""
Problem Statement: Leetcode problem no. 801

You are given two integer arrays of the same length nums1 and nums2. 
In one operation, you are allowed to swap nums1[i] with nums2[i].
For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. 
An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

Example 1:
Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation: 
Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4] which are both strictly increasing.

"""


if __name__ == '__main__':
    nums1 = [1,3,5,4]
    nums2 = [1,2,3,7]

    # insert -1 to the beginning of the list
    nums1.insert(0, -1)
    nums2.insert(0, -1)

    # Test the recursive function
    swapped = 0 # represents whether previous index are swapped or not
    print(f"Minimum number of operations: {swap_recursion(nums1, nums2, 1, swapped)}\n") # 1 represents the starting index

    # Test the Top-down DP(Memoization) function
    n = len(nums1)
    swapped = 0 # represents whether previous index are swapped or not
    dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
    print(f"Minimum number of operations: {swap_memoization(nums1, nums2, 1, swapped, dp)}\n") # 1 represents the starting index

    # Test the Bottom-up DP(Tabulation) function
    print(f"Minimum number of operations: {swap_tabulation(nums1, nums2)}\n")

    # Test the space optimized function
    print(f"Minimum number of operations: {swap_space_optimized(nums1, nums2)}\n")
