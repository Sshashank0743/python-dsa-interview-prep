def find_count(nums):
    count = 0
    for num in nums:
        if num > 6:
            count += 1

    return count




nums = [5, 10, 15, 20, 7, 16, 3, 9]


'''
Time Complexity:
O(n)

Space Complexity:
O(1)
'''