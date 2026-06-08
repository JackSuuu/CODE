import sympy as sp

# 1. 定义符号变量（可选）
λ = sp.symbols('λ')

# 2. 定义矩阵 A
A = sp.Matrix([
    [5, 1, 2, 0],
    [-3, -1, -1, 0],
    [-10, -2, -4, 0],
    [-5, -1, -2, 0],
])

# 3. 计算 Jordan Normal Form 和变换矩阵
J, P = A.jordan_form(calc_transform=True)

# 4. 输出结果
print("Jordan form J:")
sp.pprint(J)

print("\nTransformation matrix P:")
sp.pprint(P)

# 可验证：J = P⁻¹ * A * P