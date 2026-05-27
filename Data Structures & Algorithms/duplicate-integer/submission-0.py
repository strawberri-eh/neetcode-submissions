class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fk = set()
        for i in nums:
            if i in fk: return True
            fk.add(i)
        return False