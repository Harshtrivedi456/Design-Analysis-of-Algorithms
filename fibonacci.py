def fib_memo(n, dp={}):
    if n <= 1:
        return n
    if n in dp:   
        return dp[n]
    dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp)
    return dp[n]

n = int(input())
print("Fibonacci:", fib_memo(n))
