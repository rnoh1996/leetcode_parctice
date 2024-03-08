# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# Follow-up: Could you solve the problem in linear time and in O(1) space?

###########################################################################################################################

# My Initial Answer
def my_majorityElement(nums):
    elements = {}

    for el in nums:
        if el in elements:
            elements[el] += 1
        else:
            elements[el] = 1

    return elements

# This approach to finding the majority element by using a dictionary to count the occurrences of each element is straightforward and works correctly. 
# However, it's not the most efficient in terms of space complexity, especially given the follow-up challenge to solve the problem in O(1) space. 
# The current solution has a space complexity of O(n) because it potentially stores a count for every unique element in the input array.

# Inefficiencies in My Approach:
# 1) Space Complexity: As mentioned, the current approach uses additional space proportional to the number of unique elements in the input array.
# 2) Unnecessary Counting: Once an element's count exceeds n/2, I could theoretically stop counting and return that element as the majority element, 
#    but the current approach counts all elements first.

# I could've done this
def my_majorityElement2(nums):
    majority = len(nums) / 2
    elements = {}

    for el in nums:
        if el in elements:
            elements[el] += 1
        else:
            elements[el] = 1

        if elements[el] >= majority:
            return el

    return elements

# The improved version (my_majorityElement2) addresses the time complexity issue by checking the count of each element 
# as it iterates through the array and returning early if it finds the majority element. 
# This is an optimization over the initial approach since it potentially reduces the number of operations if the majority element 
# is found before iterating through the entire array. However, the space complexity remains O(n) in the worst case.

###########################################################################################################################

# Revised Answer
def revised_majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# To further optimize, especially to achieve O(1) space complexity, you can use the "Boyer-Moore Voting Algorithm". 
# This algorithm finds the majority element without needing extra space for a dictionary. 
# The idea is to maintain a count that adds 1 for a candidate element and subtracts 1 for every other element. 
# When the count reaches 0, a new candidate is chosen from the remaining elements. 
# Due to the majority element condition (appearing more than ⌊n / 2⌋ times), the candidate by the end of the array is guaranteed to be the majority element.