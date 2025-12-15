def twoSum(numbers,target):
    l = 0
    r = len(numbers) - 1
    while(l < r):
        if (numbers[l] + numbers[r]) > target:
            r -= 1
            continue
        if (numbers[l] + numbers[r]) < target:
            l += 1
            continue
        break
    return [l+1,r+1]

# call
numbers = [2,7,11,15];
target = 9
print(twoSum(numbers,target))