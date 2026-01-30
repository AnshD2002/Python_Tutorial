#POD: Interleave the First Half of the Queue with Second Half
#Timestamp: 2026-01-30 06:23:31.790576
import math
from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        q = deque(q)
        n = len(q)
        mid = n // 2
        first_half = []
        for _ in range(mid):
            first_half.append(q.popleft())
        for i in range(mid):
            q.append(first_half[i])
            q.append(q.popleft())
        return q


    
obj = Solution()
print(obj.rearrangeQueue(q=[2, 4, 3, 1]), "2 3 4 1")
print(obj.rearrangeQueue([3, 5]), "3 5")