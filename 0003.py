class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        ans = 0
        i,j = 0,0
        while (i <len(s) and j < len(s)):
            if s[j] not in hash_map:
                hash_map[s[j]] = 1
                j+= 1
                ans = max(ans,j-i)
            else:
                del hash_map[s[i]]
                i+= 1
        return ans
