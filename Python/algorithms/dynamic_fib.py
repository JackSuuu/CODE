
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def dynamic_fibonacci(n):
    if n <= 1:
        return n
    return dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number for {n} is {dynamic_fibonacci(n)}")