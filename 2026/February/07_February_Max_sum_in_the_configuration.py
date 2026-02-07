#POD: Max sum in the configuration
#Timestamp: 2026-02-07 05:14:58.404710

class Solution:
    def maxSum_1(self, arr): 
        # Code here
        sum_arr = []
        l = len(arr)
        for i in range(len(arr)):
            sum = 0
            arr.append(arr[i])
            narr = arr[i:(i+l)]
            for i in range(len(narr)):
                sum = sum+ (i*narr[i])
            sum_arr.append(sum)
        sum_arr.sort(reverse=True)
        return sum_arr[0]
    
    def maxSum(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        current_val = sum(i * arr[i] for i in range(n))
        max_val = current_val
        
        for i in range(1, n):
            current_val = current_val + total_sum - n * arr[n - i]
            if current_val > max_val:
                max_val = current_val
                
        return max_val
    
obj = Solution()
print(obj.maxSum_1([3, 1, 2, 8]))
print(obj.maxSum([3, 1, 2, 8]))