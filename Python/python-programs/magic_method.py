class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass(value={self.value})"

# Example usage
obj = MyClass(42)
print(obj)  # Output: MyClass(value=42)
