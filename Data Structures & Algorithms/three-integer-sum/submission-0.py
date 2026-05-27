class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for ai, a in enumerate(nums):
            if ai > 0 and nums[ai] == nums[ai-1]:
                continue
            bc = -a

            l = ai + 1
            r = len(nums)-1

            while l<r:
                if nums[l] + nums[r] < bc:
                    l+=1
                elif nums[l] + nums[r] > bc:
                    r-=1
                else:
                    ans.add(tuple(sorted((nums[ai], nums[l], nums[r]))))
                    l+=1
                    r-=1
        
        return [list(t) for t in ans]