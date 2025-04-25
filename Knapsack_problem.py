# Using recursion
def knapsack_recursion(weight, value, index, capacity):
    # Base case
    if index == 0:
        if weight[0] <= capacity:
            return value[0]
        else:
            return 0
        
    include = (value[index] + knapsack_recursion(weight, value, index - 1, capacity - weight[index])) if weight[index] <= capacity else 0
    exclude = 0 + knapsack_recursion(weight, value, index - 1, capacity)

    return max(include, exclude)

    
# Using Top-Down Dynamic Programming (Memoization)
def knapsack_memoization(weight, value, index, capacity, dp):
    # Base case
    if index == 0:
        if weight[0] <= capacity:
            return value[0]
        else:
            return 0
        
    # Check if the result already computed or not
    if dp[index][capacity] != -1:
        return dp[index][capacity] 
        
    include = (value[index] + knapsack_memoization(weight, value, index - 1, capacity - weight[index], dp)) if weight[index] <= capacity else 0
    exclude = 0 + knapsack_memoization(weight, value, index - 1, capacity, dp)

    dp[index][capacity] = max(include, exclude)
    return dp[index][capacity]
        

# Using Bottom-Up Dynamic Programming (Tabulation)
def knapsack_tabulation(weight, value, n, capacity):
    # Initialize a dp array
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    # Base cases
    for w in range(weight[0], capacity + 1):
        if weight[0] <= capacity:
            dp[0][w] = value[0]
        else:
            dp[0][w] = 0
    
    # Fill the dp array iteratively
    for index in range(1, n):
        for w in range(0, capacity + 1):
            include = (value[index] + dp[index - 1][w - weight[index]]) if weight[index] <= w else 0
            exclude = 0 + dp[index - 1][w]

            dp[index][w] = max(include, exclude)

    return dp[n - 1][capacity]


# Space optimized solution
def knapsack_space_optimized(weight, value, n, capacity):
    # Initialize two arrays to for rows
    prev = [0] * (capacity + 1)
    curr = [0] * (capacity + 1)

    # Base case
    for w in range(weight[0], capacity + 1):
        if weight[0] <= capacity:
            prev[w] = value[0]
        else:
            prev[w] = 0

    for index in range(1, n):
        for w in range(0, capacity + 1):
            include = (value[index] + prev[w - weight[index]]) if weight[index] <= w else 0
            exclude = 0 + prev[w]

            curr[w] = max(include, exclude)
        
        prev = curr
    
    return prev[capacity]


# Further optimized solution
def knapsack_further_space_optimized(weight, value, n, capacity):
    # Initialize array to for rows
    curr = [0] * (capacity + 1)

    # Base case
    for w in range(weight[0], capacity + 1):
        if weight[0] <= capacity:
            curr[w] = value[0]
        else:
            curr[w] = 0

    for index in range(1, n):
        for w in range(capacity, 0, -1):
            include = (value[index] + curr[w - weight[index]]) if weight[index] <= w else 0
            exclude = 0 + curr[w]

            curr[w] = max(include, exclude)
        
    return curr[capacity]



"""
Problem Statement:
A thief is robbing a stor and can carry maximal weight of 'W' into his knapsack.
There are 'N' items and the ith item weighs wi and is of value vi.
Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.
"""

if __name__ == '__main__':
    n = 4
    w = 5
    weights =[1, 2, 4, 5]
    values = [5, 4, 8, 6]

    # Test the recursive function
    print(f"Maximum value within the knapsack capacity is {knapsack_recursion(weights, values, n - 1, w)}\n")  # 'n - 1' as staring from last index/item

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(w + 1)] for _ in range(n)]
    print(f"Maximum value within the knapsack capacity is {knapsack_memoization(weights, values, n - 1, w, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Maximum value within the knapsack capacity is {knapsack_tabulation(weights, values, n, w)}\n")

    # Test the space optimized function
    print(f"Maximum value within the knapsack capacity is {knapsack_space_optimized(weights, values, n, w)}\n")
    
    # Test the further space optimized function
    print(f"Maximum value within the knapsack capacity is {knapsack_further_space_optimized(weights, values, n, w)}\n")