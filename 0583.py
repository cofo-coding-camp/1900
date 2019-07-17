class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp =[[0]*(len2+1) for i in range(len1+1)]
        
        for i in range(len1+1):
            for j in range(len2+1):
                if i ==0 or j == 0:
                    dp[i][j] = 0
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return len1+len2-2*dp[len1][len2]
   
