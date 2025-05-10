# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Roberto Ochoa Cuevas

def findMaxConsecutiveOnes(nums):

    count = 0;
    maxCount = 0;

    for num in nums:
        if num == 1:
            count+= 1
            if count > maxCount:
                maxCount = count;
        else:
            if count > maxCount:
                maxCount = count;
            count = 0;
    return maxCount;
        

nums = [1,0,1,1,1];
print(findMaxConsecutiveOnes(nums));