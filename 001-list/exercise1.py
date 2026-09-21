def excercise_1(nums):
    first = nums[0]
    nums.append(100)
    nums.insert(0, 50)
    return first

'''
# Time Complexity:
O(1)
O(1) because the function directly accesses nums[0], regardless of how many elements are in the input array.

#Space Complexity:
O(1)
O(1) because the function doesn't create any additional data structure whose size depends on the input.

#Why:
Because I have to do only 1 action to perform.
'''