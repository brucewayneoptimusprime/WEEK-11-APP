def print_diamond_pattern(n):
    for i in range(1, n, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    for i in range(n, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

# Example usage:
n = 5
print_diamond_pattern(n)
