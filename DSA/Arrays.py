arr = [] # variable for array
arr = [2, 3, 4] # Initiates array

# Fixed-size array (Cannot alter or update the size of an array) - Also known as STATIC ARRAYS
fixedArray = [0] * 5

# Dynamic Sized Arrays (Array size changes as per user requirements)
dynamicArray = []

# Array Traversal - Involes visiting all the ellemnts of the array once
for i in range(len(arr)): # len(arr) returns the number of elements (3)
    print(arr[i], end=" ")
print()

for index, value in enumerate(arr): # Another way to do this
    print(value, end=" ")
print()

# Insertion in Array - Insert one or multiple elements at any position in the array
newElement = 5
pos = 3
arr.insert(pos, newElement)
print("Updated List:", arr)

# Deletion in Array - Delete an element at any index in an array
valueToDelete = 2
if valueToDelete in arr: # If valueToDelete is inside arr
    arr.remove(valueToDelete)
    print(arr)
else:
    print("Element not found")

# Searching in Array - Traverse over an array and search for an element
def find_element(arr, n, key): # "arr" is the array. "n" is the lenght of the array. "key" is the element to be found
    for i in range(n):
        if arr[i] == key:
            print("found it")
            return i
    return -1 # If the loops completes without finding "key", return -1

x = find_element(arr, len(arr), 3)
print(x)

"""
APPLICATIONS OF ARRAY
- They are used in the implementation of other data structures such as array lists, heaps, hash tables, vectors, and matrices.
- Database records are usually implemented as arrays.
- It is used in lookup tables by computer.
"""

# OTHER EXERCISES
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    nums[:] = nums[:k]
    return nums
    

nums = [3,2,2,3]
target = 2
x = removeElement(nums, target)
print(x)

def maxProfit(prices):
    max_profit = 0
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            print(prices[buy], prices[sell])
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
    return max_profit

prices = [7,1,5,3,6,4]
x = maxProfit(prices)
print(f"max profit {x}")
