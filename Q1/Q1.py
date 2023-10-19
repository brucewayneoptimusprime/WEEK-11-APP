def find_largest_two(arr):
    first_max = second_max = float('-inf')
    
    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num < first_max:
            second_max = num
    
    return first_max, second_max

# Example usage:
arr = [3, 7, 1, 9, 5, 4]
first, second = find_largest_two(arr)
print("First largest:", first)
print("Second largest:", second)
