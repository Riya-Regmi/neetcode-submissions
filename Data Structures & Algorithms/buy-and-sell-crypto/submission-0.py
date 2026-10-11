class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=min(prices)#1
        day=0
        output=0
        while day<=len(prices):
            if  min_price==prices[day]:
                max_price=max(prices[day:]) #
                output=max_price-min_price
                return output
            else:
                day+=1


        