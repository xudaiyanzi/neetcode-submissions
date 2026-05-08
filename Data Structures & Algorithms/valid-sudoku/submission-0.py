class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create a set list for row, column, and sub-box
        r_set = [set() for _ in range(9)]
        c_set = [set() for _ in range(9)]
        sub_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                src = (r // 3) * 3 + c // 3
                if board[r][c] in r_set[r] or board[r][c] in c_set[c] or board[r][c] in sub_set[src]:
                    return False
                
                r_set[r].add(board[r][c])
                c_set[c].add(board[r][c])
                sub_set[src].add(board[r][c])
            
        return True


