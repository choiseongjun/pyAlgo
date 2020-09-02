import sys
def maxProfit(prices):
    profit=0
    #min_price=float('inf')
    min_price=sys.maxsize

    for price in prices:
        min_price=min(min_price,price)
        print(min_price)
        profit=max(profit,price-min_price)
    return profit

prices=[7,1,5,3,6,4]
a=maxProfit(prices)
print(a)