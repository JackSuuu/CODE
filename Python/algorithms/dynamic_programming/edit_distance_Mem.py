# Recursive function to find minimum edit distance between two strings
# The Memorization version using a memo table to remember precompute steps
def min_dis_rec(s1, s2, m, n, memo):
    if m == 0:
        return n

    if n == 0:
        return n
    
    if memo[m][n] is not None:
        return memo[m][n]
    
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = min_dis_rec(s1, s2, m - 1, n - 1, memo)
    else:
        insert = min_dis_rec(s1, s2, m, n - 1, memo)    # Insert
        remove = min_dis_rec(s1, s2, m - 1, n, memo)    # Remove
        replace = min_dis_rec(s1, s2, m - 1, n - 1, memo) # Replace
        # ! The important step to store insert, remove, replace into memo
        memo[m][n] = 1 + min(insert, remove, replace)
        # print(memo)
        
    return memo[m][n] # Return the computed minimum distance

# Function to initalize memorization table and start the recursive function
def min_dis(s1, s2):
    m, n = len(s1), len(s2)
    # init memo
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    return min_dis_rec(s1, s2, m, n, memo)

# Main function to execute the program
if __name__ == "__main__":
    s1 = "GEEXSFRGEEKKS" # First string
    s2 = "GEEKSFORGEEKS" # Second string

    print(min_dis(s1, s2))