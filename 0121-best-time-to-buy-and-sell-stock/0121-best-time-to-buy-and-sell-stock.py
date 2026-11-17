class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        volume = len(prices)
        buy = prices[0]
        profit = 0
        for i in range(1,volume):
            if prices[i]<buy:
                 buy = prices[i]
            elif ((prices[i])-buy)>profit:
                profit = (prices[i])-buy
        return profit