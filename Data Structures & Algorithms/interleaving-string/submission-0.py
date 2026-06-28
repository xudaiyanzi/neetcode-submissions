class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, t = len(s1), len(s2), len(s3)
        if m + n != t:
            return False
        dp = {}

        def dfs(i, j):
            if i + j == t:
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            take_s1, take_s2 = False, False
            if i < m and s1[i] == s3[i + j] and dfs(i + 1, j):
                take_s1 = True
            else: 
                take_s1 = False

            if j < n and s2[j] ==s3[i + j] and dfs(i, j + 1):
                take_s2 = True
            else:
                take_s2 = False
            dp[(i, j)] = take_s1 or take_s2
            return dp[(i, j)]
        
        return dfs(0, 0)
            


