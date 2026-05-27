class Solution:
    def trap(self, height: List[int]) -> int:
        pm = [height[0]]
        for i,v in enumerate(height):
            if i>0:
                pm.append(max(pm[i-1], v))
        ep = [height[-1]]
        for i,v in enumerate(height[::-1]):
            if i > 0:
                ep.append(max(ep[i-1], v))
        
        ep = ep[::-1]

        ans = 0
        for i in range(len(height)):
            ans += min(ep[i],pm[i]) - height[i]
        return ans