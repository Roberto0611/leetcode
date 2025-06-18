# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


# approach 1
def containsDuplicate(nums):
    contador = {}

    for num in nums:
        contador[num] = contador.get(num,0) + 1
        if contador[num] == 2:
            return True
    return False


# call 
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))