def count_even(nums):
    count = 0

    for num in nums:
        if num %2 == 0:
            count += 1

    return count


'''
Time Complexity:
O(n)

Space Complexity:
O(1)
'''