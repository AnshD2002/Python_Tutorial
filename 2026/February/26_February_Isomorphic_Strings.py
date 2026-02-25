#POD: Isomorphic Strings
#Timestamp: 2026-02-26 00:31:10.683842

# Given two strings s1 and s2 consisting of only
# lowercase English letters and of equal length,
# check if these two strings are isomorphic to
# each other. If the characters in s1 can be
# changed to get s2, then two strings, s1 and s2
# are isomorphic. A character must be completely
# swapped out for another character while maintaining
# the order of the characters. A character may map to
# itself, but no two characters may map to the same
# character

class Solution:
    def areIsomorphic(self,s: str, t: str) -> bool:
        #code here
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in s_map and s_map[char_s] != char_t:
                return False
            if char_t in t_map and t_map[char_t] != char_s:
                return False
            s_map[char_s] = char_t
            t_map[char_t] = char_s

        return True

obj = Solution()
print(obj.areIsomorphic("egg","add"))