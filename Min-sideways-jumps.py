# Using recursion
def minSideJumps_recursion(obstacle, currlane, currpos):
    n = len(obstacle) - 1

    # Base case
    if currpos == n:
        return 0
    
    if obstacle[currpos + 1] != currlane:
        return minSideJumps_recursion(obstacle, currlane, currpos + 1)
    else:
        # sideways jumps
        ans = float('inf')
        for i in range(1, 4): # range is 1 to 3 as there are three lanes only
            if (currlane != i) and (obstacle[currpos] != i):
                ans = min(ans, 1 + minSideJumps_recursion(obstacle, i, currpos))
        
        return ans


# Using Top-Down Dynamic Programming (Memoization)
def minSideJumps_memoization(obstacle, currlane, currpos, dp):
    n = len(obstacle) - 1

    # Base case
    if currpos == n:
        return 0
    
    # Check if the result already computed or not 
    if dp[currlane][currpos] != -1:
        return dp[currlane][currpos]
    
    if obstacle[currpos + 1] != currlane:
        return minSideJumps_memoization(obstacle, currlane, currpos + 1, dp)
    else:
        # sideways jumps
        ans = float('inf')
        for i in range(1, 4): # range is 1 to 3 as there are three lanes only
            if (currlane != i) and (obstacle[currpos] != i):
                ans = min(ans, 1 + minSideJumps_memoization(obstacle, i, currpos, dp))
        
        dp[currlane][currpos] = ans
        return dp[currlane][currpos]


# Using Bottom-Up Dynamic Programming (Tabulation)
def minSideJumps_tabulation(obstacle):
    n = len(obstacle) - 1

    # Initialize a dp array
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(4)]

    # Base case
    dp[0][n], dp[1][n], dp[2][n], dp[3][n] = 0, 0, 0, 0

    for currpos in range(n - 1, -1, -1):
        for currlane in range(4):
            if obstacle[currpos + 1] != currlane:
                dp[currlane][currpos] = dp[currlane][currpos + 1]
            else:
                # sideways jumps
                ans = float('inf')
                for i in range(1, 4): # range is 1 to 3 as there are three lanes only
                    if (currlane != i) and (obstacle[currpos] != i):
                        ans = min(ans, 1 + dp[i][currpos])
                
                dp[currlane][currpos] = ans

    return min(dp[2][0], 1 + dp[1][0], 1 + dp[3][0])


# Space optimized solution
def minSideJumps_space_optimized(obstacle):
    n = len(obstacle) - 1

    # Initialize the array
    curr = [float('inf') for _ in range(4)]
    nxt = [float('inf') for _ in range(4)]

    # Base case
    nxt[0], nxt[1], nxt[2], nxt[3] = 0, 0, 0, 0

    for currpos in range(n - 1, -1, -1):
        for currlane in range(4):
            if obstacle[currpos + 1] != currlane:
                curr[currlane] = nxt[currlane]
            else:
                # sideways jumps
                ans = float('inf')
                for i in range(1, 4): # range is 1 to 3 as there are three lanes only
                    if (currlane != i) and (obstacle[currpos] != i):
                        ans = min(ans, 1 + nxt[i])
                
                curr[currlane] = ans
        
        nxt = curr

    return min(nxt[2], 1 + nxt[1], 1 + nxt[3])


"""
Problem Statement: ( leetcode 1824)

There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. 
However, there could be obstacles along the way.
You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. 
If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

Note: There will be no obstacles on points 0 and n.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, 
the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

"""

if __name__ == '__main__':
    currlane, currpos = 2, 0 # as per the question

    obstacle = [0,1,2,3,0] # output: 2
    # obstacle = [0,1,1,3,3,0] # output: 0

    # Test the recursive function
    print(f"Minimum side ways jumps: {minSideJumps_recursion(obstacle, currlane, currpos)}\n")

    # Test the Top-down DP(Memoization) function
    dp = [[-1 for _ in range(len(obstacle))] for _ in range(4)]
    print(f"Minimum side ways jumps: {minSideJumps_memoization(obstacle, currlane, currpos, dp)}\n")

    # Test the Bottom-up DP(Tabulation) function
    print(f"Minimum side ways jumps: {minSideJumps_tabulation(obstacle)}\n")

    # Test the space optimized function
    print(f"Minimum side ways jumps: {minSideJumps_space_optimized(obstacle)}\n")
