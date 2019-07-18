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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max = 0
        for i in range(len(s)):
            hash = {}
            terminate = True

            for j in range(i,len(s)):

                if s[j] not in hash.keys():
                    hash[s[j]] = 1
                else:
                    terminate = False
                    break
            if terminate:
                l = j-i+1
            else:
                l = j-i
            if max < l:
                max = l

                i = j+1
        return max




