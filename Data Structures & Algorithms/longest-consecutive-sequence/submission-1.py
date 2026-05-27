class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)

        ans = 0
        lans = 1
        for v in nums:
            if v-1 not in ns:
                while v+lans in ns:
                    lans+=1
                ans = max(ans, lans)
                lans = 1
        
        return ans