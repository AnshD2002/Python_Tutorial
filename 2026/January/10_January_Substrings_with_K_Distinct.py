#POD: Substrings with K Distinct
#Timestamp: 2026-01-10 22:29:17.781700

class Solution:
    def countSubstr(self, s, k):
        def atMost(n):
            if n < 0:
                return 0
            
            left = 0
            count = 0
            distinct_count = 0
            freq_map = {}
            
            for right in range(len(s)):
                char_right = s[right]
                
                if freq_map.get(char_right, 0) == 0:
                    distinct_count += 1
                freq_map[char_right] = freq_map.get(char_right, 0) + 1
                
                while distinct_count > n:
                    char_left = s[left]
                    freq_map[char_left] -= 1
                    if freq_map[char_left] == 0:
                        distinct_count -= 1
                    left += 1
                
                count += (right - left + 1)
            
            return count

        return atMost(k) - atMost(k - 1)





obj = Solution()
print(obj.countSubstr("abcba", 2))