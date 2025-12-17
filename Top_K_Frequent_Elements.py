from collections import Counter
import heapq

def topKFrequent(nums,k):
    numsDic = Counter(nums)
    return heapq.nlargest(k,numsDic.keys(),key=numsDic.get)

# call
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))