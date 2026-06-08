def cyk_algorithm(grammar, start_symbol, word):
    n = len(word)
    
    # Create a DP table
    dp = [[set() for _ in range(n)] for _ in range(n)]
    
    # Fill table for single characters
    for i, char in enumerate(word):
        for lhs, rhs in grammar.items():
            if char in rhs:
                dp[i][i].add(lhs)
    
    # Fill table for longer substrings
    for length in range(2, n + 1):  # Substring lengths from 2 to n
        for i in range(n - length + 1):  # Start index
            j = i + length - 1  # End index
            
            for k in range(i, j):  # Split point
                for lhs, rhs in grammar.items():
                    for production in rhs:
                        print(dp)
                        if len(production) == 2:  # Check if it's a rule A → BC
                            B, C = production
                            if B in dp[i][k] and C in dp[k + 1][j]:
                                dp[i][j].add(lhs)
    
    # Check if start symbol derives the full string
    return start_symbol in dp[0][n - 1]


# Define the CNF grammar as a dictionary
grammar = {
    "S": {("A", "B"), ("B", "C")},
    "A": {("B",), "a"},
    "B": {("C",), "b"},
    "C": {"a"}
}

# Example test
word = "ba"
print(cyk_algorithm(grammar, "S", word))  # Output: True
