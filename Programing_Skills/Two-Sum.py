'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

LeetCode problem link: https://leetcode.com/problems/two-sum/description/

'''

# Initialize the function
def twoSum(nums, target):
    for index,number in enumerate(nums):
        for index2,x in enumerate(nums):
            if number + x == target and index2 != index:
                return [index,index2]

# Call the function
print(twoSum([3,3],6))