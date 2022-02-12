from typing import List


def maxProfit(prices: List[int]) -> int:
    buy = prices[0]
    sell = prices[0]
    profit = 0

    for i in prices:
        if i < buy:
            buy = i
            sell = i
        elif i > sell:
            sell = i
            profit = max(sell - buy, profit)

    print(profit)


maxProfit([3, 2, 6, 5, 0, 3])
