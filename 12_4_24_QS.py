def sort_list(data):
  if len(data) <= 1:
    return data

  # Choose the first element (alternative approaches exist)
  reference_value = data[0]

  # Partitioning
  left = [i for i in data[1:] if i <= reference_value]
  right = [i for i in data[1:] if i > reference_value]

  # Recursive sorting
  return sort_list(left) + [reference_value] + sort_list(right)

# Example usage
my_list = [8, 3, 1, 4, 2, 7, 6, 5]
sorted_list = sort_list(my_list)

print(f"Sorted list: {sorted_list}")