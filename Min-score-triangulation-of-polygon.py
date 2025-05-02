# Using recursion
def score_recursion(v, i, j):
    # Base case: if there is only two nodes
    if i + 1 == j:
        return 0
    
    ans = float('inf') # to store the minimum score
    k = i + 1
    while k < j:
        ans = min(ans, v[i] * v[j] * v[k] + score_recursion(v, i, k) + score_recursion(v, k, j))
        k += 1
    
    return ans


# Using Top-Down Dynamic Programming (Memoization)
def score_memoization(v, i, j, dp):
    # Base case
    if i + 1 == j:
        return 0
    
    # Check if the result already computed or not
    if dp[i][j] != -1:
        return dp[i][j]

    ans = float('inf') # to store the minimum score
    k = i + 1
    while k < j:
        ans = min(ans, v[i] * v[j] * v[k] + score_memoization(v, i, k, dp) + score_memoization(v, k, j, dp))
        k += 1

    dp[i][j] = ans
    return dp[i][j]


# Using Bottom-Up Dynamic Programming (Tabulation)
def score_tabulation(v):
    n = len(values)

    # Initialize a dp array with 0
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 2, n):
            ans = float('inf') # to store the minimum score
            k = i + 1
            while k < j:
                ans = min(ans, v[i] * v[j] * v[k] + dp[i][k] + dp[k][j])
                k += 1

            dp[i][j] = ans
    
    return dp[0][n - 1]


"""
Problem Statement: leetcode problem no. 1039

You have a convex n-sided polygon where each vertex has an integer value. 
You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.
Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. 
Note that no other shapes other than triangles are allowed in the division. 
This process will result in n - 2 triangles.
You will triangulate the polygon. 
For each triangle, the weight of that triangle is the product of the values at its vertices. 
The total score of the triangulation is the sum of these weights over all n - 2 triangles.
Return the minimum possible score that you can achieve with some triangulation of the polygon.

"""

if __name__ == '__main__':
    # values = [1,2,3] # output: 6
    values = [3,7,4,5] # output: 144

    # Test the recursive function
    print(f"Minimum score: {score_recursion(values, 0, len(values) - 1)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(len(values))] for _ in range(len(values))]
    print(f"Minimum score: {score_memoization(values, 0, len(values) - 1, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Minimum score: {score_tabulation(values)}\n")
