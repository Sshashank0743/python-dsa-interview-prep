def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []

'''
Time Complexity = O(n²)

Space Complexity = O(1)

'''


# ascending order
def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return(sorted([nums[i], nums[j]]))

    return []


'''
Time Complexity = O(n²)

Space Complexity = O(1)

'''


# descending order
def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return(sorted([nums[i], nums[j]], reverse=True))

    return []


'''
Time Complexity = O(n²)

Space Complexity = O(1)

'''