def edit_dist_dp(s1, s2):
    m, n = len(s1), len(s2)

    # Create a table to store results of sub-problems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the known entries in dp[][]
    # If one string is empty, then answer
    # is length of the other string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the rest of dp[][]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]: # 0 -> match
                # note that both match and switch takes the same cell
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1], # insertion
                    dp[i - 1][j], # deletion
                    dp[i - 1][j - 1] # substitution
                )
    
    return dp[m][n]

s1 = "GEEXSFRGEEKKS"
s2 = "GEEKSFORGEEKS"
print(edit_dist_dp(s1, s2))