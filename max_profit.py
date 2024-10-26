def maxProfit(prices) -> int:
    if not prices:
        return 0
    min_price = float('inf')
    profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price
    return profit

if __name__ == '__main__':
    prices = [2,5,1,5]
    print(maxProfit(prices))
