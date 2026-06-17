class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        n = len(s)

        def dfs(i):
            if i == n:
                return True
            if i in dp:
                return dp[i]

            res = False
            for w in wordDict:
                if s[i:].startswith(w):
                    if dfs(i + len(w)):
                        res = True
                        break
            dp[i] = res
            return res
        
        return dfs(0)