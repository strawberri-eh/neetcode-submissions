class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zr = 0
        for v in nums:
            if v!= 0 :
                p*=v
            else:
                zr+=1
        
        ans = []
        for v in nums:
            if v==0:
                ans.append(0) if zr-1 else ans.append(p)
            else:
                if zr!=0:
                    ans.append(0)
                else:
                    ans.append(p//v)

        
        return ans