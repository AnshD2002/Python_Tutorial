#POD: Last Moment Before All Ants Fall Out
#Timestamp: 2026-02-05 00:15:31.621578

class Solution:
    def getLastMoment(self, n, left, right):
        max_left = max(left) if left else 0
        max_right = max([n - x for x in right]) if right else 0
        return max(max_left, max_right)
    
obj = Solution()
print(obj.getLastMoment(n=9, left=[5], right=[4]))