"""
MERGE SORT EXPLANATION:
It is usually done recursively. We will break our problem as if we were using Divide & Conquer.
Merge sort has a time complexity of O(logN) which is optimal for comparison based algorithms.

STEPS:
1. Split array in half
2. Call Merge Sort on each half to sort them recursively
3. Merge both sorted halves into one sorted array


"""

def mergeSort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        # Recursion
        mergeSort(left_array)
        mergeSort(right_array)

        # Merge
        i = 0   # Left Most Element in the LEFT ARRAY (index)
        j = 0   # Left Most Element in the RIGHT ARRAY (index)
        k = 0   # Merged Array Index

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]: # If element from left array is less than element from right array
                array[k] = left_array[i] # Save value inside merged array
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        
        # If there are no more elements to compare (either left to right or right to left), we will append remaining elements
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


    return array

array = [8, 6, 1, 20, 70, 90, 60, 158, 12, 3 ,5]
x = mergeSort(array)
print(x)