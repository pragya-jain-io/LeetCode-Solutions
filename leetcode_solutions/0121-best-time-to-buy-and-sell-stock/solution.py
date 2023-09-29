class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n=len(prices)
        b,s=0,1
        max=0
        while s<len(prices) and b<len(prices):
            if (prices[s]-prices[b])<0:
                b+=1
                s=b+1
            else:
                if (prices[s]-prices[b])>max:
                    max=(prices[s]-prices[b])
                s+=1
        return max
