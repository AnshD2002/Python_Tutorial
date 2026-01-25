#POD: Josephus problem
#Timestamp: 2026-01-25 18:37:40.792167

class Solution:
    def josephus(self,n, k):
        # code here
        arr = list(range(1, n + 1)) 
        index = 0 
        while len(arr) > 1:
            index = (index + k - 1) % len(arr)
            arr.pop(index)
            
        return arr[0]


obj = Solution()
print(obj.josephus(7,3))  # Expected output: 4