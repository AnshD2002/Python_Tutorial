#POD: Stream First Non-repeating
#Timestamp: 2026-01-29 00:01:37.208285

from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        frequency = {}
        queue = deque()
        result = []
        
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
            
            if frequency[char] == 1:
                queue.append(char)
            
            while queue and frequency[queue[0]] > 1:
                queue.popleft()
            
            if queue:
                result.append(queue[0])
            else:
                result.append('#')
                
        return "".join(result)
					
obj = Solution()
print(obj.firstNonRepeating('aabc'))