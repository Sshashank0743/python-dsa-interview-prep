def linear_search(nums):
    target = 10
    for i in range(len(nums)):
        if nums[i] == target:
             return i

    return -1

'''
Why return -1?
Because -1 means:
I searched the list but couldn't find the target.

Time Complexity:
O(n)

Space Complexity:
O(1)

'''


nums = [10, 25, 7, 40, 15]
target = 40