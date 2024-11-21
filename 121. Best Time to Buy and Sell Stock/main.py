import os
import sys
from typing import List

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, ".."))
from checker import runTestCases


def maxProfit(prices: List[int]) -> int:
    max_profit = 0

    # initialize $p_i$ as the first price
    min_price = prices[0]

    for price in prices:
        # potential $p_i$
        if price < min_price:
            min_price = price
        # compute largest gap with respect to $p_i$
        if price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


def main():
    test_cases = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]

    runTestCases(maxProfit, test_cases)


if __name__ == "__main__":
    main()
