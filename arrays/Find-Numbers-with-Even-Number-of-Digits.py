# Given an array nums of integers, return how many of them contain an even number of digits.
def findNumbers(nums):
    count = 0;
    for num in nums:
        if len(str(num)) % 2 == 0:
            count+=1

    return count;

nums = [555,901,482,1771];
print(findNumbers(nums))