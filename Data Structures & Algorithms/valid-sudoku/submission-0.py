class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col  = defaultdict(set)

        sqm = defaultdict(set)
        def _get_sq_pres(r,c, ele):
            sq = (r//3)*3 + (c//3)
            if ele in sqm[sq]:
                return True
            sqm[sq].add(ele)
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                ele = board[r][c]
                if ele == ".": continue
                if ele in row[r] or ele in col[c] or _get_sq_pres(r,c,ele):
                    return False
                row[r].add(ele)
                col[c].add(ele)
        
        return True