class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        st = 0
        en = l-1

        while st < l and en >0:

            ste = s[st]
            ene = s[en]

            if not ste.isalnum():
                st+=1
                continue
            if not ene.isalnum():
                en-=1
                continue
            
            if ste.lower()!=ene.lower():
                return False
            else:
                st+=1
                en-=1
        
        return True
