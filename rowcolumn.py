def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_index = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            # else not needed since dp[i][j] already 0

    return s1[end_index - max_len:end_index] if max_len > 0 else ""

# Example input (space separated)
s1 = input().strip()
s2 = input().strip()
print(longest_common_substring(s1, s2))
