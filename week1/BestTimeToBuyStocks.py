# 121. Best time to buy and sell Stock
'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

# approach 1 
'''
def maxProfit(prices):
    buy = 0;

    # search smaller value
    for index,price in enumerate(prices):
        if price < prices[buy]:
            buy = index

    print(f'Buy encontrado en la posicion {buy}')

    sell = buy;

    # search bigger value from smaller
    for i in range(buy + 1,len(prices)):
        if prices[i] > prices[sell]:
            sell = i;

    print(f'sell encontrado en la posicion {sell}')    

    return prices[sell] - prices[buy]
'''

# approach 2 (o (n)^2)
'''def maxProfit(prices):
    sell = 0
    maxprofit = 0

    for buy in range(len(prices)):
        for price in prices[buy+1:]:
            print(prices[buy+1:])
            if price > prices[buy]:
                profit = price - prices[buy]
                if profit > maxprofit:
                    maxprofit = profit;
    return maxprofit'''

# approach 3 
'''def maxProfit(prices):
    minPrice = prices[0];
    maxProfit = 0;
    maxN = 0;

    for index,price in enumerate(prices):
        maxN = 0;
        if minPrice > price:
            minPrice = price
        for i in prices[index:]:
            if i > maxN:
                maxN = i;
        if maxN - minPrice > maxProfit:
            maxProfit = maxN - minPrice;
    return maxProfit;'''

# approach 4 (TESTS PASSED )
def maxProfit(prices):
    minPrice = prices[0];
    maxProfit = 0;

    for index,priceToday in enumerate(prices):
        if minPrice > priceToday:
            minPrice = priceToday
        if priceToday - minPrice > maxProfit:
            maxProfit = priceToday - minPrice

    return maxProfit;

# testcase
prices = [7,1,5,3,6,4]
print(maxProfit(prices))