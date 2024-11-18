"""
BUBBLE SORT EXPLANATION:

 #A - For i in range 0 to indexing_lenght
 #B - If the item to the left (unsorted_list[i]) is greater than the item to the right (unsorted_list[i + 1])
 #C - "sorted" variable becomes FALSE
 #D - Values are switched. For example, if LEFT is 5 and RIGHT is 3, then RIGHT value becomes 5 and LEFT value becomes 3.

 This sorting algorithm is simple, but really slow for large datasets
"""

def bubble(unsorted_list):
    indexing_length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length): # A
            if unsorted_list[i] > unsorted_list[i+1]: # B
                sorted = False # C
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i] # D
    return unsorted_list

list_a = [5, 2, 1, 0, 10, 85, 60, 12, 45, 32]
x = bubble(list_a)
print(x)