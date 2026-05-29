class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visiting = set()
        rows = len(board)
        columns = len(board[0])

        def backtrack(r, c, start):
            if start == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= columns:
                return False

            if board[r][c] != word[start] or (r,c) in visiting:
                return False
            
            visiting.add((r, c))
            
            Found = backtrack(r + 1, c, start + 1) or backtrack(r - 1, c, start + 1) or backtrack(r, c + 1, start + 1) or backtrack(r, c - 1, start + 1) 

            visiting.remove((r, c))
            return Found
        
        for r in range(rows):
            for c in range(columns):
                if backtrack(r, c, 0):
                    return True
        
        return False