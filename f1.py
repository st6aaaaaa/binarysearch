'''

Given an array of integers nums which is sorted in ascending
order, and an integer target, write a function to search target in
nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.   '''


def binarysearch(nums,target):
    low = -1
    high = len(nums)

    while low != high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid
        else :
            high = mid - 1
    return -1
