def test_1(nums):
    print(nums[0])


'''
Time Complexity:
O(1)

Space Complexity:
O(1)

Why:
Because I have to do only 1 action to perform.
'''



def test_2(nums):
    for num in nums:
        print(num)

'''
Time Complexity:
O(n)

Space Complexity:
O(1)

Why:
The loop runs once for every element in nums.
Therefore, if there are n elements, the loop executes n times.
The function does not create any additional data structure
that grows with the input size, so extra space is O(1).
'''


def test_3(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(nums[i], nums[j])

'''
Time Complexity:
O(n²)

Space Complexity:
O(1)

Why:
The outer loop runs n times, and for each iteration of the outer loop, the inner loop also runs n times. Therefore, the total number of operations is n × n = n². 
No additional data structure grows with the input, so space is O(1).
'''



def test_4(nums):
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
The algorithm eliminates approximately half of the remaining search space during each iteration, so the time complexity is O(log n). 
It only uses the variables left, right, and middle, so the extra space complexity is O(1).
'''