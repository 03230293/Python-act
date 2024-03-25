def bubble_sort(arr):
    n=len(arr) #7

    for i in range(n):
        for j in range(0, n-i-1): #starts from 0
            if arr[j]>arr[j+1]:
                arr[j], arr [j+1]= arr[j+1], arr[j] #sorts

arr=[66,34,25,12,22,11,90]

bubble_sort(arr)

print("Sorted array:")
for i in range(len(arr)):
    print(arr[i])

    #n*n and O(1)