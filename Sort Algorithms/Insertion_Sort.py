import random
"""
INSERTION SORT EXPLANATION:

1. Work left to right
2. Examine each item and compare it to items on it's left <-- THEY ARE BEING COMPARED FROM THE ITEMS ON THE ELEMENT'S LEFT SIDE!
3. INSERT the item in the correct position in the array

#A - While the element from the LEFT side is HIGHER than the "value_to_sort", then do the SWAP.

EXAMPLE:
a = [10, 5]
- index 1 (5) is the "value_to_sort" and index 0 is the LEFT element of index 1
- Then, we compare then. First the LEFT element against the "value_to_sort".
- The LEFT element is HIGHER than the "value_to_sort", so we place "value_to_sort" value into that LEFT element.

RESULT: [5, 10]

This one is a little bit faster than Bubble and Selection sort algorithms
"""
def insertion_sort(list_a):
    index_length = range(1, len(list_a))
    for i in index_length:
        value_to_sort = list_a[i]

        while list_a[i - 1] > value_to_sort and i > 0: # A
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1
    return list_a


a = [10, 25, 100, 89, 2, 1, 67, 3, 4, 80, 11]
b = insertion_sort(a)
print(b)