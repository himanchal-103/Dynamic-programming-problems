# Fibonacci Series using Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

# Fibonacci Series using Top-Down Dynamic Programming (Memoization)
def fibonacci_memoization(n, memo={}):
    # Check if the result is already in the memo dictionary
    if n in memo:
        return memo[n]
    
    # Base case: return n if it is 0 or 1
    if n <= 1:
        return n
    else:
        # Recursive case: calculate Fibonacci and store it in the memo dictionary
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]
    

# Fibonacci Series using Bottom-Up Dynamic Programming (Tabulation)
def fibonacci_tabulation(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Initialize a list to store Fibonacci numbers up to n and set the first two Fibonacci numbers
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    # Fill the dp array using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # Return the nth Fibonacci number
    return dp[n]


# Fibonacci series space optimized solution
def fibonacci_space_optimized(n):
    if n <= 1:
        return n
    
    # Initialize two variables to store the previous two Fibonacci numbers
    previous2, previous1 = 0, 1
    
    # Iterate from 2 to n and update the variables
    for _ in range(2, n + 1):
        previous2, previous1 = previous1, previous2 + previous1
    
    # Return the nth Fibonacci number
    return previous1


if __name__ == '__main__':
    n = 10  # Change this value to compute Fibonacci for different numbers

    # Test the recursive function
    print("Fibonacci series using recursion:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
    print("\n")

    # Test the Top-down DP(Memoization) function
    print("Fibonacci series using Top-down DP (Memoization):")
    print(fibonacci_memoization(n - 1), end=" ")
    print("\n")

    # Test the Bottom-up DP(Tabulation) function
    print("Fibonacci series using Bottom-up DP (Tabulation):")
    print(fibonacci_tabulation(n - 1))
    print("\n")

    # Test the space optimized function
    print("Fibonacci series using space optimized function:")
    print(fibonacci_space_optimized(n - 1))
