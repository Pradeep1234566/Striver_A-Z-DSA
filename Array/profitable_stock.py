'''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

    This file contains the code for the above problem 
'''

def profit(stocks, n):
    min = float('inf')
    maximum_profit = -float('inf')
    for i in range(n):
        if min > stocks[i]:
            min = stocks[i]
        tp = stocks[i] - min
        maximum_profit = max(tp, maximum_profit)
    return maximum_profit

n = int(input())
stocks = []

for i in range(n):
    stocks.append(int(input()))

print(profit(stocks, n))