def twoSum(nums, target):
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    for i in range(len(nums)):
        y = target - nums[i]

        if y in h and h[y] != i:
            return [i, h[y]]

nums, target = [2,7,11,15], 9
x = twoSum(nums, target)
print(x)