class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        key = [0 for i in range(26)]
        hm = defaultdict(list)

        def _genk(w):
            nk = [0 for i in range(26)]
            for c in w:
                nk[ord(c)-ord('a')] += 1
            return tuple(nk)

        for w in strs:
            key = _genk(w)
            hm[key].append(w)

        return list(hm.values())