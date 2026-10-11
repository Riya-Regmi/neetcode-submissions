class Solution:
    def maxProfit(self, prices: List[int]) -> int: #prices=[7,1,5,3,6,4]
        min_price=prices[0] #7
        profit=0
        for idx,price in enumerate(prices[1:]):
            if price<min_price:
                min_price=price
            if price-min_price>profit:
                profit=price-min_price #5
        return profit



        