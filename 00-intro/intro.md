TIME
↓
How many times does my code execute?

SPACE
↓
How much EXTRA memory does my code need?



# Time Complexity
Time complexity tells us how the amount of work performed by an algorithm grows when the input becomes larger.

## Real-life example
Imagine you have a list of people:
Rahul
Amit
Priya
Neha
...


You want to find Amit.

You might check:
Shashank ❌
Rahul ❌
Amit ✅

3 checks.

Now imagine there are:
### 1,000 people.

In the worst case, you may need to check:
Person 1
Person 2
Person 3
...
Person 1000

The amount of work grows with the number of people.

Now here we call this:
O(n)   "Big O of n


What is n?
n simply represents:
the size of the input


For example:
nums = [10, 20, 30, 40, 50]

Here:
n = 5

If:
nums = [10, 20, 30, ..., 1000]

then:
n = 1000

So when we say:
O(n)


we're basically saying:
The amount of work grows approximately in proportion to the input size.


# Space Complexity
Space complexity tells us how much additional memory an algorithm needs as the input grows.