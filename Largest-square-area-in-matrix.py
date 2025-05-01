# Using recursion
def square_recursion(mat, i, j):
    # Base case: index should be inside the range
    if (i >= len(mat)) or (j >= len(mat[0])):
        return 0
    
    # move to right, diagonal, down
    right = square_recursion(mat, i, j + 1)
    diagonal = square_recursion(mat, i + 1, j + 1)
    down = square_recursion(mat, i + 1, j)

    return (1 + min(right, diagonal, down)) if mat[i][j] == 1 else 0


# Using Top-Down Dynamic Programming (Memoization)
def square_memoization(mat, i, j, dp):
    # Base case: index should be inside the range
    if (i >= len(mat)) or (j >= len(mat[0])):
        return 0
    
    # Check if the result already computed or not
    if dp[i][j] != -1:
        return dp[i][j]
    
    # move to right, diagonal, down
    right = square_memoization(mat, i, j + 1, dp)
    diagonal = square_memoization(mat, i + 1, j + 1, dp)
    down = square_memoization(mat, i + 1, j, dp)
    
    # Update the value in dp
    dp[i][j] = (1 + min(right, diagonal, down)) if mat[i][j] == 1 else 0
    return dp[i][j]


# Using Bottom-Up Dynamic Programming (Tabulation)
def square_tabulation(mat, row, column):
    # Initialize a dp array with 0
    dp = [[0 for _ in range(column + 1)] for _ in range(row + 1)]
    val = 0

    # Fill the array iteratively
    for i in range(row - 1, -1, -1):
        for j in range(column - 1, -1, -1):
            right = dp[i][j + 1]
            diagonal = dp[i + 1][j + 1]
            down = dp[i + 1][j]

            dp[i][j] = (1 + min(right, diagonal, down)) if mat[i][j] == 1 else 0
            val = max(val, dp[i][j])
    
    return val


# Space optimized solution
def square_space_optimized(mat, row, column):
    # Initialize two arrays
    curr = [0] * (column + 1)
    nxt = [0] * (column + 1)
    val = 0

    # Fill iteratively
    for i in range(row - 1, -1, -1):
        for j in range(column - 1, -1, -1):
            right = curr[j + 1]
            diagonal = nxt[j + 1]
            down = nxt[j]

            curr[j] = (1 + min(right, diagonal, down)) if mat[i][j] == 1 else 0
            val = max(val, curr[j])
        
        nxt = curr
    
    return val



"""
Problem Statement:
Given a binary matrix of size n*m, find out the maximum size of square sub-matrix with all 1's.

"""

if __name__ == '__main__':
    n = 2 # row
    m = 2 # column
    mat = [[1, 1],
           [1, 1]]
    # mat = [[0, 0],
    #        [0, 0]]
    
    # Test the recursive function
    print(f"Size of largest squared sub matrix is {square_recursion(mat, 0, 0)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(m + 1)] for _ in range(n)]
    print(f"Size of largest squared sub matrix is {square_memoization(mat, 0, 0, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Size of largest squared sub matrix is {square_tabulation(mat, n, m)}\n")

    # Test the space optimized function
    print(f"Size of largest squared sub matrix is {square_space_optimized(mat, n, m)}\n")

