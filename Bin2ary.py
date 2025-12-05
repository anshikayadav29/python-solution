# Binary Search - Iterative
def binary_search_iter(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# Binary Search - Recursive
def binary_search_rec(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, high)
    else:
        return binary_search_rec(arr, target, low, mid - 1)


# Driver Code
arr = [2, 5, 7, 10, 14, 18, 21]
target = 14

print("Iterative:", binary_search_iter(arr, target))
print("Recursive:", binary_search_rec(arr, target, 0, len(arr)-1))
