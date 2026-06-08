def DPLL(clauses, symbols, model):
    # Check if all clauses are satisfied
    if not any(clauses):
        return True

    # Check if any clause is unsatisfied
    if any(not clause for clause in clauses):
        return False

    # Select a symbol from symbols
    symbol = symbols[0]

    # Recurse with symbol assigned as True
    result = DPLL([clause for clause in clauses if symbol not in clause], symbols[1:], model + [(symbol, True)])
    if result:
        return True

    # Recurse with symbol assigned as False
    result = DPLL([clause for clause in clauses if f'~{symbol}' not in clause], symbols[1:], model + [(symbol, False)])
    return result


def dpll_solver(clauses):
    symbols = set()
    for clause in clauses:
        for literal in clause:
            symbols.add(literal)

    symbols = list(symbols)
    return DPLL(clauses, symbols, [])


# Example usage
clauses = [['A', '~B', 'C'], ['A', 'B', '~C'], ['~A', 'B', 'C']]
result = dpll_solver(clauses)

if result:
    print("Satisfiable. Model:", result)
else:
    print("Unsatisfiable.")
