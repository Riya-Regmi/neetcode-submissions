class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0] #10
        profit=0
        for idx,price in enumerate(prices[1:]):
            if price-min_price>profit: 
                profit=price-min_price 
            else:
                min_price=price 
        return profit



        