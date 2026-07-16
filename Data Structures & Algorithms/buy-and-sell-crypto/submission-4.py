class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        if length==1:
            return 0

        difference=0
        if prices[1]-prices[0]>0:
            difference=prices[1]-prices[0]

        lowest=0
        for i in range(1,length):
            if prices[lowest]>prices[i]:
                lowest=i
            elif prices[i]-prices[lowest]>difference:
                difference=prices[i]-prices[lowest]
        return difference