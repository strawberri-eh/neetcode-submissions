class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = { val: idx for idx, val in enumerate(nums)}

        for i,v in enumerate(nums):
            diff = target - v
            if diff in hmap:
                di = hmap[diff]
                if di == i: continue
                return [i, di] if i < di else [di,i]
            