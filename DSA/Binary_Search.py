def iterative_binary_search(array, target):
    left = 0
    right = len(array) - 1 # Last element of the array

    while (left <= right):
        mid = (right + left) // 2 # Sum indexes and returns an average value

        if array[mid] == target:
            return mid # return index target
        elif array[mid] < target:
            left = mid + 1 # update left pointer
        else:
            right = mid - 1 # update right pointer
    return -1 # target is not in the array

def recursion_binary_search(arr, target, left, right): # Involves the function calling itself with updated parameters
    if left > right:
        return - 1 # Base case: Target not found
    mid = left + (right - left) // 2 # Gets middle index from array
    if arr[mid] == target: # Done!
        return mid
    elif arr[mid] < target: # If arr[mid] is smaller than the target, search in the RIGHT HALF of the list
        return recursion_binary_search(arr, target, mid + 1, right) # Checks right half
    else: # Else, if arr[mid] is larger than target, search in the LEFT HALF of the list
        return recursion_binary_search(arr, target, left, mid - 1) # Checks left half
    

customArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = iterative_binary_search(customArray, 3)
y = recursion_binary_search(customArray, 7, 0, len(customArray) - 1)
print(f"Iterative Binary Search Result: {x}\nRecursion Binary Search Result: {y}")