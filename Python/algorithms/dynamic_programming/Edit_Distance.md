# Three main approach to implement

1. plain recursion
2. plain recursion + memorization
3. dynamic programming (Bottom-up)

## DP (Bottom-Up)

Use a table to store solutions of subproblems to avoiding recalculate the same subproblems multiple times.

1. Choosing Dimensions of Table: depends on input parameter, for Edit Distance since we have parameter m, n, so we need to construct a 2D table **dp[][]**
2. Choosing Correct size of Table: The range of parameters from 0 to m, 0 to n, so we choose **(m + 1)*(n + 1)**
3. Filling the table: consist two stages, 1 - table init, 2 - building solution

```python
if (s1[i – 1] == s2[j – 1]) dp[i][j] = dp[i – 1][j – 1];

if (s1[i – 1] != s2[j – 1]) dp[i][j] = 1 + min(dp[i][j – 1], dp[i – 1][j], dp[i – 1][j – 1]); 
```

4. Returning final soltion: after filling the table iteratively, 

