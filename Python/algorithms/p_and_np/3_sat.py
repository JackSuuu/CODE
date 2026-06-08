import random

def max_3_sat(clauses):
    """
    Greedy de-randomized algorithm for Max 3-SAT.
    Args:
        clauses (list of tuples): Each clause is a tuple of literals (e.g., (1, -2, 3)).
                                  Positive integers represent variables, negative integers represent negated variables.
    Returns:
        assignment (dict): A satisfying assignment for the variables.
    """
    # Extract all variables from the clauses
    variables = set(abs(literal) for clause in clauses for literal in clause)
    assignment = {var: None for var in variables}

    # De-randomized greedy algorithm
    for var in variables:
        # Calculate expected satisfaction for x_var = 0 and x_var = 1
        satisfied_if_0 = 0
        satisfied_if_1 = 0

        for clause in clauses:
            if any(literal > 0 and assignment[abs(literal)] is True for literal in clause) or \
               any(literal < 0 and assignment[abs(literal)] is False for literal in clause):
                # Clause is already satisfied
                continue

            # Check satisfaction if var is assigned 0 or 1
            if var in map(abs, clause):
                if any(literal == var for literal in clause):
                    satisfied_if_1 += 1
                if any(literal == -var for literal in clause):
                    satisfied_if_0 += 1

        # Assign the value that maximizes satisfaction
        if satisfied_if_1 >= satisfied_if_0:
            assignment[var] = True
        else:
            assignment[var] = False

    return assignment


# Example usage
if __name__ == "__main__":
    # Example: (x1 OR NOT x2 OR x3) AND (NOT x1 OR x2 OR NOT x3)
    clauses = [
        (1, -2, 3),
        (-1, 2, -3),
        (1, 2, -3),
        (-1, -2, 3)
    ]
    result = max_3_sat(clauses)
    print("Satisfying assignment:", result)