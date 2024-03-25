def birnary_search(arr, x):
    left=0
    right=len(arr) -1

    while left <= right:
        mid =(left+right)//2 #takes a whole no.
        
        if arr[mid]==x:
            return mid
        
        if arr[mid]<x:
            left=mid+1

        if arr[mid]>x:
            right=mid-1

    return -1

arr=[2,3,4,6,8,10,12]
x=10

result=birnary_search(arr, x) 

if result!=-1:
    print("Element fount at index", result)
else:
    print("Element not found")