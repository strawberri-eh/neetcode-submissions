class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minll = 2**32
        minl = []
        for v in prices:
            minll = min(minll, v)
            minl.append(minll)
        
        maxll = -1
        maxl = []
        for v in prices[::-1]:
            maxll = max(maxll, v)
            maxl.append(maxll)

        maxl = maxl[::-1]
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, maxl[i]-minl[i])

        return ans