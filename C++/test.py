import sympy as sp

def polynomial_with_roots(N, m):

    x = sp.symbols('x')

    p = sp.prod([(q*x + 1) for q in range(1, N+1)])

    coeffs = sp.Poly(p, x).all_coeffs()

    coeffs.reverse()

    return int(coeffs[m]) if m < len(coeffs) else 0


print(polynomial_with_roots(40, 40))
print(polynomial_with_roots(2, 0))