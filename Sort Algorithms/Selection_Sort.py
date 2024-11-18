"""
SELECTION SORT EXPLANATION:
We use this sort algorithm when we want to sort an array in ascending order. During each iteration we'll select the smallest item from the unsorted partition and move it to the sorted partition.

#A - Starts with whole unsorted list
#B - Loop that goes through each element in the list, EXCEPT THE LAST ONE!
#C - Assumes teh current element is the smallest
#D - Loop starts comparing all the elements after "i" from (i+1) to the end of the list to find the smallest element
#E - If we find an element that is smaller than the one at the current "min_value", we update "min_value" to point to that smaller element's index
#F - Assigns "min_value" with new smaller element's index
#G - If the "min_value" is different from "i"
#H - Swap elements. This places teh smalles element found in it's correct position (i)

This is A LOT better than the Bubble Sort. Time complexity is still high because of the nested loops
"""
def selection_sort(list_a):
    indexing_lenght = range(0, len(list_a) - 1) # A

    for i in indexing_lenght: # B
        min_value = i # C
        for j in range(i + 1, len(list_a)): # D
            if list_a[j] < list_a[min_value]: # E
                min_value = j # F
        
        if min_value != i: # G
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value] # H
    return list_a # I

a = [8, 7, 5, 3, 4, 9, 10, 50, 60, 70]
x = selection_sort(a)
print(x)
