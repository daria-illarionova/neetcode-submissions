class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        max_profit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            if profit > max_profit:
                max_profit = profit

            if prices[sell] < prices[buy]:
                # update buy,sell ptrs (sell updated later)
                # move buy ptr to the index of sell, buy = sell 
                # buy will refer to the current min value found
                buy = sell
            # sell ptr always updated at the end of each itteration
            sell += 1

        return max_profit