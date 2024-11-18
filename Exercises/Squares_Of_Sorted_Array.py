"""
PROBLEM: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
SOLUTION: Used Two Pointers technique to get squared value of each element and then sorted in ascending order

"""
def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    sortedVal = [0] * len(nums)
    position = len(nums) - 1

    while left < right:
        sorted_left = nums[left] ** 2
        sorted_right = nums[right] ** 2

        if sorted_left > sorted_right:
            sortedVal[position] = sorted_left
            left += 1
        else:
            sortedVal[position] = sorted_right
            right -= 1
        position -= 1

    return sortedVal
            
    

a = [-4,-1,0,3,10]

x = sortedSquares(a)
print(x)