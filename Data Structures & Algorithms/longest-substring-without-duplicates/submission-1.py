class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) in (0,1):
            return 0 if len(s) == 0 else 1
        st = 0
        seen = set()
        for e in range(len(s)):
            while s[e] in seen:
                seen.remove(s[st]) ## shorten from left side
                st+=1
            seen.add(s[e])
            ans = max(ans, e - st + 1)

        return ans
