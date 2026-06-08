# Chomsky Normal Form (CNF) Grammar
grammar = {
    "NP": {("Det", "Nom")},
    "Nom": {"book", "orange", ("AP", "Nom")},
    "AP": {"heavy", "orange", ("Adv", "A")},
    "A": {"heavy", "orange"},
    "Det": {"my"},
    "Adv": {"very"}
}

# Input sentence
sentence = ["my", "very", "heavy", "orange", "book"]

# CYK Algorithm Implementation

def cyk_parse(grammar, sentence):
    n = len(sentence)
    
    # DP table: dp[i][j] stores non-terminals that derive substring sentence[i:j+1]
    dp = [[set() for _ in range(n)] for _ in range(n)]
    
    # Step 1: Fill table for single words - diagonal cell
    for i, word in enumerate(sentence):
        for lhs, rhs in grammar.items():
            if word in rhs:
                dp[i][i].add(lhs) # [i][i] -> [0][0], [1][1], [2][2]

    # Step 2: Fill table for longer substrings
    for length in range(2, n + 1):  # Length from 2 to n
        for i in range(n - length + 1):  # Start index
            j = i + length - 1  # End index
            # * for print the dp table out, to see process
            print("\n".join(["\t".join([str(cell) for cell in row]) for row in dp]))
            print("=======================================")
            for k in range(i, j):  # Split point
                for lhs, rhs in grammar.items():
                    for production in rhs:
                        if isinstance(production, tuple) and len(production) == 2:
                            B, C = production
                            # ** Key DP step, to compare construct cell based on CNF **
                            if B in dp[i][k] and C in dp[k + 1][j]:
                                dp[i][j].add(lhs)

    # Print the CYK table
    for row in dp:
        print(row)

    # Check if start symbol "NP" derives the full sentence
    return "NP" in dp[0][n - 1]

# Run the CYK parser
result = cyk_parse(grammar, sentence)
print("\nSentence belongs to the grammar:", result)
