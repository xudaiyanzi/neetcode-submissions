class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_indx = (r // 3) * 3 + c // 3

                if val in row_sets[r] or val in col_sets[c] or val in box_sets[box_indx]:
                    return False
                row_sets[r].add(val)
                col_sets[c].add(val)
                box_sets[box_indx].add(val)
        
        return True

                