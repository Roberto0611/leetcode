# 53. Maximum subarray
def maxSubArray(nums):
    max = nums[0]
    actualSum = 0

    for index,i in enumerate(nums):
        actualSum = actualSum + nums[index]

        if actualSum > max:
            max = actualSum
        
        if 0 > actualSum:
            actualSum = 0
    
    return max
        

nums = [5,4,-1,7,8]
print(maxSubArray(nums))