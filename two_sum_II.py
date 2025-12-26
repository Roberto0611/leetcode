def twoSum(numbers,target):
    a = 0
    b = len(numbers) - 1

    while a < b:
        if numbers[a] + numbers[b] > target:
            b -= 1
            continue
        if numbers[a] + numbers[b] < target:
            a += 1
            continue
        return [a+1,b+1]

# call
numbers = [2,7,11,15];
target = 9
print(twoSum(numbers,target))