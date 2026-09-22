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


def exercise_2(nums):
    total = 0
    for num in nums:
        total += num

    return total


'''
# Time Complexity:
O(n)

#Space Complexity:
O(1)

#Why:
The loop executes n times so time complexity would be O(n).
The function doesn't create additional data structure so space complexity would be O(1).
'''



def exercise_3(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return largest


'''
# What does this algorithm do?
This algorithm will run n times till it reaches bigger than largest number.

# Time Complexity:
O(n)

#Space Complexity:
O(1)

#Why:
The loop executes n times so time complexity would be O(n).
The function doesn't create additional data structure so space complexity would be O(1).
'''


def exercise_4(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1

'''
# Time Complexity:
O(n)

#Space Complexity:
O(1)

#Why:
The loop executes exponentially n times so time complexity would be O(n).
The function doesn't create additional data structure so space complexity would be O(1).
'''
