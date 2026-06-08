# assert - something should be true
def square(x):
    return x * x

# Test the square function
result = square(5)
assert result == 25, "Square function is incorrect"

# Print "correct" if the assertion passes
print("correct")