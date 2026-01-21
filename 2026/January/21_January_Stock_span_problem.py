#POD: Stock span problem
#Timestamp: 2026-01-21 20:29:18.257689

class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        sol = []
        
        for i in range(n):
            span = 0
            j = i
            while j >= 0 and arr[j] <= arr[i]:
                span += 1
                j -= 1
            sol.append(span)
            
        return sol



obj = Solution()
print("Hello ",obj.calculateSpan(arr=[10, 4, 5, 90, 120, 80]))
