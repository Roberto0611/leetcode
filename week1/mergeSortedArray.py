# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# approach 1 - I give up trying this

# def merge(nums1,m,nums2,n):
#     i=0 # inserted numbers from nums2
#     nums2 = nums2[:n]
#     if nums2 != []:
#         if m != 0:
#             for index,num in enumerate(nums1):
#                 if nums2[i] <= num or index >= m and num == 0:
#                     nums1.insert(index,nums2[i])
#                     nums1.pop()
#                     print(nums1)
#                     if i == len(nums2) - 1:
#                         break
#                     i += 1
#         else:
#             nums1.insert(0,nums2[0]) 
#             nums1.pop()       
#     return nums1

# approach 2 
def merge(nums1,m,nums2,n):
    # Last index of num1
    last = m + n - 1

    # merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -=1

    # fill nums1 with the leftovers in nums2
    while n > 0:
        nums1[last] = nums2[n - 1]
        n,last = n - 1, last - 1



# call

# testcase 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2= [2,5,6]
n = 3

# testcase 2
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# testcase 3 
# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3

# testcase 4
# nums1 = [1,0]
# m = 1
# nums2 = [2]
# n = 1

print(merge(nums1,m,nums2,n))