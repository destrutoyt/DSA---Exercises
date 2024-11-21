def merge(nums1, m, nums2, n):
    # Start merging from the back
    i = m - 1  # Last index of actual nums1 values
    j = n - 1  # Last index of nums2
    k = m + n - 1  # Last index of nums1 total

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Fill nums1 with remaining nums2 elements, if any
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        
    return nums1


nums1, nums2 = [1,2,3,0,0,0], [2,5,6]
x = merge(nums1, 3, nums2, 3)
print(x)