## :book: Best Time to Buy and Sell Stock

### Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i` day.
You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day** in the future to sell that stock.
Return the *maximum profit* you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Solution
Consider a list of prices $\\{p_1,\dots,p_i,\dots,p_j,\dots,p_n\\}$ and suppose that $(p_i,p_j)$ is the solution, i.e., $p_j-p_i$ is the maximum profit. Then the following properties holds:

- $p_1,\dots,p_{i-1}$ cannot be smaller than $p_i$, otherwise $p_i$ will not be the solution. Therefore, we try to find potential $p_i$ starting from $p_1$.
- $p_{i+1},\dots,p_{j-1}, p_{j+1},\dots, p_n$ cannot be larger than $p_j$, otherwise $p_j$ will not be the solution. Therefore, we try to find the largest gap given some potential $p_i$.
- $p_{i+1},\dots,p_{j-1}$ cannot be smaller than $p_i$, otherwise $p_i$ will not be the solution. Therefore, if $p_i$ is the solution, we are guaranteed to find $p_j$ before finding the next potential $p_i$.

Together, we try to find a smaller price as a potential $p_i$ by the first property, then compute the largest gap with $p_i$ by the second property. If $p_i$ is the solution, then this process is guaranteed to find the solution by the third property. We only need one loop to look through all potential $p_i$.

```python
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
```
