arr = [10, 15, 20, 5, 30] 
target = 30
def linear_search(arr, target): #parametern- ar and target
    for i in range(len(arr)):
        if arr[i] == target:
            print (i)
    return -1

# result = linear_search(arr, target)
linear_search(arr, target)

 #o(n) and o(1)

# if result != -1: 
#     print("Element found at index", result)
# else: 
#     print("Element not found")