# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

###########################################################################################################################

# """
# Do not return anything, modify nums in-place instead.
# """

# My Initial Answer
def my_rotate(nums, k):
    for i in range(k):
        el = nums.pop()
        nums.insert(0, el)

# is inefficient primarily due to its use of pop() and insert(0, el) inside a loop that iterates k times. 
# Here's why these operations contribute to inefficiency:

# 1) pop() operation: While pop() without an index (or with -1 as an index) is generally efficient because it removes 
#    and returns the last element of the list, the inefficiency comes from its repeated use within the loop.

# 2) insert(0, el) operation: This is particularly costly in terms of time complexity. 
#    Inserting an element at the beginning of a list (index 0) in Python is an O(n) operation because it requires shifting 
#    all the existing elements in the list one position to the right to accommodate the new element. 
#    When you do this inside a loop that runs k times, it compounds the inefficiency, especially for large lists and large values of k.

# 3) Repeatedly modifying the list: Each iteration of the loop modifies the list, 
#    which becomes increasingly inefficient as the size of the list (n) and the number of rotations (k) grow.

###########################################################################################################################

# Revised Answer
def revised_rotate(nums, k):
    n = len(nums)
    k %= n  # In case k is larger than the list size

    # Helper function to reverse a portion of the list
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    # Step 1: Reverse the entire list
    reverse(0, n-1)
    # Step 2: Reverse the first k elements
    reverse(0, k-1)
    # Step 3: Reverse the remaining elements
    reverse(k, n-1)

# It is much more efficient because, reversing a section of a list in Python does not require shifting elements in the way that inserting 
# elements at the beginning of the list does. Instead, reversing is typically implemented by swapping elements in place, which is much more efficient.

# When you reverse a list or a part of it, you generally swap the element at the start with the element at the end, then move both pointers inward and 
# continue swapping until you meet in the middle. This operation is done in place, meaning no additional space is needed to store temporary elements 
# (beyond the few variables needed for the operation, which only require constant space).