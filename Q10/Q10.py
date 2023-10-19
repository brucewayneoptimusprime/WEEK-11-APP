def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
        return sequence

# Example usage:
n = 10  # Change this to the number of terms you want
fib_sequence = generate_fibonacci_sequence(n)
print("Fibonacci sequence:", fib_sequence)
