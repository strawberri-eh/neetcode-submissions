class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        bket = [[] for _ in range(len(nums)+1)]

        for key,v in c.items():
            bket[v].append(key)

        
        ans = []
        for r in bket[::-1]:
            if r:
                ans.extend(r)
            if len(ans) >= k:
                return ans[:k]
        