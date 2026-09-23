"""
Big-O Exercises
Python DSA Interview Preparation

Instructions:
1. Read each function.
2. Do NOT run the code initially.
3. Predict the time complexity.
4. Predict the space complexity.
5. Write your reasoning in the ANSWERS section.
"""

# ============================================================
# EXERCISE 1
# ============================================================

def exercise_1(nums):
    return nums[0]

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



# ============================================================
# EXERCISE 2
# ============================================================

def exercise_2(nums):
    for num in nums:
        print(num)

'''
# Time Complexity:
O(n)

# Space Complexity:
O(1)

# Why:
The loop runs once for every element in nums.
Therefore, if there are n elements, the loop executes n times.
The function does not create any additional data structure
that grows with the input size, so extra space is O(1).
'''


# ============================================================
# EXERCISE 3
# ============================================================

def exercise_3(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(nums[i], nums[j])

'''
# Notice that there are two loops.

# Think of it like this:
Outer loop
   │
   ├── Inner loop runs completely
   │
   ├── Inner loop runs completely
   │
   └── Inner loop runs completely

# Time Complexity:
O(n²)

# Space Complexity:
O(1)

# Why:
The outer loop runs n times, and for each iteration
of the outer loop, the inner loop also runs n times.
Therefore the total number of operations is n × n = n².

The function does not create an additional data structure
that grows with the input size, so the extra space is O(1).
'''


# ============================================================
# EXERCISE 3.1
# ============================================================
def test(nums):
    for num in nums:
        print(num)

    for num in nums:
        print(num)


'''
Time Complexity:
O(n)

Space Complexity:
O(1)

Why:
Time complexity is O(n) because two sequential loops each run n times, giving 2n operations, which simplifies to O(n). 
Space complexity is O(1) because no additional memory grows with the input size.

'''


# ============================================================
# EXERCISE 4
# ============================================================

def exercise_4(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2

        if nums[middle] == 10:
            return middle
        elif nums[middle] < 10:
            left = middle + 1
        else:
            right = middle - 1

    return -1


'''
Time Complexity:
O(log n)

Space Complexity:
O(1)

Why:
The algorithm eliminates approximately half of the remaining search space on every iteration, so the time complexity is O(log n).
It only uses a few variables (left, right, middle), so the extra space complexity is O(1).

'''


# ============================================================
# EXERCISE 5
# ============================================================

def exercise_5(nums):
    for i in range(len(nums)):
        print(nums[i])

    for i in range(len(nums)):
        print(nums[i])


'''
Time Complexity:
O(n)

Space Complexity:
O(1)

Why:
Time complexity is O(n) because two sequential loops each run n times, giving 2n operations, which simplifies to O(n). 
Space complexity is O(1) because no additional memory grows with the input size.

'''

# ============================================================
# EXERCISE 6
# ============================================================

def exercise_6(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])


'''
Time Complexity:
O(n²)

Space Complexity:
O(1)

Why:
The inner loop runs fewer times for each successive value of i, but the total number of iterations is approximately n²/2,
which simplifies to O(n²). Only constant extra variables are used, so space complexity is O(1).

'''

# ============================================================
# YOUR ANSWERS
# ============================================================

"""
Exercise 1:
Time Complexity:
Space Complexity:
Why:


Exercise 2:
Time Complexity:
Space Complexity:
Why:


Exercise 3:
Time Complexity:
Space Complexity:
Why:


Exercise 4:
Time Complexity:
Space Complexity:
Why:


Exercise 5:
Time Complexity:
Space Complexity:
Why:


Exercise 6:
Time Complexity:
Space Complexity:
Why:
"""