def knapsack(weights, values, W):
    n = len(values)
    
    # DP table (n+1) x (W+1)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W], dp


# Example Usage
weights = [1, 3, 4, 5]   # weights of items
values = [1, 4, 5, 7]    # values of items
W = 7                    # max capacity

max_value, dp_table = knapsack(weights, values, W)
print("Maximum Value:", max_value)
