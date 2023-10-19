def count_occurrences(arr, element):
    count = arr.count(element)
    return count

# Example usage:
arr = [1, 2, 2, 3, 2, 4, 5, 2]
element = 2
count = count_occurrences(arr, element)
print(f"{element} occurs {count} times in the array.")
