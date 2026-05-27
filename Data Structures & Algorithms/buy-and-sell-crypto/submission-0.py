class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        s,e = 0,1

        while e < len(prices):
            if prices[s] < prices[e]:
                tans = prices[e]-prices[s]
                ans = max(tans, ans)
            else:
                s = e
            
            e+=1
        
        return ans