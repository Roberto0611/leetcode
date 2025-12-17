def maxProfit(prices):
    lowern = prices[0]
    maxProfit = 0
    for num in prices:
        if lowern > num:
            lowern = num
        maxProfit = max(maxProfit, num - lowern)
    return maxProfit

# testcase
prices = [7,1,5,3,6,4]
print(maxProfit(prices))