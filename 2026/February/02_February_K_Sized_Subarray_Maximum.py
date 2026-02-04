#POD: K Sized Subarray Maximum
#Timestamp: 2026-02-02 00:31:57.408418

from collections import deque

class Solution:
    def maxOfSubarrays(arr, k):
        # code here
        if len(arr)==1:
            return arr
        sol = []
        i = 0
        while i <(len(arr)-k+1):
            a = arr[i:(i+k)]
            sol.append(max(a))
            i=i+1
        return sol
    
    

    def maxOfSubarrays_improved(arr, k):
        n = len(arr)
        if n == 0:
            return []
        if k == 1:
            return arr
            
        sol = []
        dq = deque()
        
        for i in range(n):
            if dq and dq[0] == i - k:
                dq.popleft()
                
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
                
            dq.append(i)
            
            if i >= k - 1:
                sol.append(arr[dq[0]])
                
        return sol



obj = Solution
print(obj.maxOfSubarrays(arr=[1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3))
print(obj.maxOfSubarrays_improved(arr=[1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3))