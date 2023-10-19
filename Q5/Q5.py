def remove_duplicates(arr):
    unique_list = []
    for item in arr:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result = remove_duplicates(original_list)
print("List with duplicates removed:", result)
