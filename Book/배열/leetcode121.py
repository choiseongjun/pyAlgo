import sys

def solution(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit,price-min_price)
    print(profit)
    return profit


if __name__ == '__main__':
    arr = [7, 1, 5, 3, 6, 4]
    solution(arr)