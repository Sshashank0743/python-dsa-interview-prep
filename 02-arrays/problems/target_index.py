def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


'''
Time complexity
O(n)

Space Complexity
O(1)

Why?
Because I will run my loop n times for checking the current num is same as my target or not. If yes then I will get the index value. O(n) in the worst case because we may need to check every element in the list once.
Space complexity is O(1) because the algorithm uses only a constant amount of extra memory and does not create any data structure that grows with the input size.
'''