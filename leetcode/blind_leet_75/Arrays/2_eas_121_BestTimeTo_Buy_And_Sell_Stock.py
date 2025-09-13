from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')     # Track lowest price seen so far
        max_profit = 0               # Track the highest possible profit

        for price in prices:
            # If current price is less than min seen so far, update min_price
            if price < min_price:
                min_price = price

            # If selling today yields better profit, update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
