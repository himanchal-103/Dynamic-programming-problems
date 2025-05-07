# Using recursion
def maxHeight_recursion(n, a, curr, prev):
    # Base case: if traversing is complete that is curr == n
    if curr == n:
        return 0
    
    # include element
    include = 0
    if (prev == -1) or (a[curr][0] >= a[prev][0] and a[curr][1] >= a[prev][1] and a[curr][2] >= a[prev][2]):
        include = a[curr][2] + maxHeight_recursion(n, a, curr + 1, curr)

    # exclude element
    exclude = maxHeight_recursion(n, a, curr + 1, prev)

    return max(include, exclude)
    

# Using Top-Down Dynamic Programming (Memoization)
def maxHeight_memoization(n, a, curr, prev, dp):
    # Base case: if traversing is complete that is curr == n
    if curr == n:
        return 0
    
    # Check if the result already computed or not 
    if dp[curr][prev + 1] != -1:
        return dp[curr][prev + 1]
    
    # include element
    include = 0
    if (prev == -1) or (a[curr][0] >= a[prev][0] and a[curr][1] >= a[prev][1] and a[curr][2] >= a[prev][2]):
        include = a[curr][2] + maxHeight_memoization(n, a, curr + 1, curr, dp)

    # exclude element
    exclude = maxHeight_memoization(n, a, curr + 1, prev, dp)

    dp[curr][prev + 1] = max(include, exclude)
    return dp[curr][prev + 1]


# Using Bottom-Up Dynamic Programming (Tabulation)
def maxHeight_tabulation(n , a):
    # Initialize a dp array
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 1)]

    # Base case already handles as array is initialized with 0

    for curr in range(n - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            # include element
            include = 0
            if (prev == -1) or (a[curr][0] >= a[prev][0] and a[curr][1] >= a[prev][1] and a[curr][2] >= a[prev][2]):
                include = a[curr][2] + dp[curr + 1][curr + 1]

            # exclude element
            exclude = dp[curr + 1][prev + 1]

            dp[curr][prev + 1] = max(include, exclude)
    
    return dp[0][0]


# Space optimized solution
def maxHeight_space_optimized(n, a):
    # Initialize a dp array
    currRow = [0] * (n + 1)
    nextRow = [0] * (n + 1)

    for curr in range(n - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            # include element
            include = 0
            if (prev == -1) or (a[curr][0] >= a[prev][0] and a[curr][1] >= a[prev][1] and a[curr][2] >= a[prev][2]):
                include = a[curr][2] + nextRow[curr + 1]

            # exclude element
            exclude = nextRow[prev + 1]

            currRow[prev + 1] = max(include, exclude)
        nextRow = currRow
    
    return nextRow[0]


"""
Problem statement: Leetcode porblem no.1691

Note: This problem is similar to the problem 'Longest increasing subsequence'.

Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). 
Choose a subset of cuboids and place them on each other.
You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. 
You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.
Return the maximum height of the stacked cuboids.

Example:
Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190
Explanation:
Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.

"""

if __name__ == '__main__':
    # cuboids = [[50,45,20],[95,37,53],[45,23,12]] # output: 190
    cuboids = [[38,25,45],[76,35,3]] # output: 76

    # Step 1: sort all dimensions for every cuboid
    sorted_cuboids = [sorted(cuboid) for cuboid in cuboids]

    # Step 2: sort the cuboids on the basis of width and length
    sorted_cuboids.sort(key=lambda x: (x[0], x[1]))
    n = len(sorted_cuboids)

    # Test the recursive function
    print(f"Maximum hieght: {maxHeight_recursion(n, sorted_cuboids, 0, -1)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(n + 2)] for _ in range(n + 1)]
    print(f"Maximum hieght: {maxHeight_memoization(n, sorted_cuboids, 0, -1, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Maximum hieght: {maxHeight_tabulation(n, sorted_cuboids)}\n")

    # Test the space optimized function
    print(f"Maximum hieght: {maxHeight_space_optimized(n, sorted_cuboids)}\n")
