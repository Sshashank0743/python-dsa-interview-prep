def find_min(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    return smallest

'''
What does the algorithm do?
It scans the entire list and keeps track of the smallest
value found so far.

Time Complexity:
O(n)

Space Complexity:
O(1)

Why:
The algorithm checks every element in the list once, so the amount of work grows linearly with the number of elements.
It only uses a constant number of variables and does not create an additional data structure that grows with the input, so the extra space is O(1).

'''