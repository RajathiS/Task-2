def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]


    max_length = 0

    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    return s1[end_index - max_length: end_index]
s1 = "Guvigeeks"
s2 = "xGuvigeeks"
result = longest_common_substring(s1, s2)
print("Common substring:", result)