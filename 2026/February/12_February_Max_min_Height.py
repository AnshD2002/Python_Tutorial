#POD: Max min Height
#Timestamp: 2026-02-12 23:35:57.196587

class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        n = len(arr)
        
        def is_feasible(target_h):
            added_height = [0] * (n + 1)
            current_waterings = 0
            total_days_used = 0
            
            for i in range(n):
                current_waterings += added_height[i]
                actual_height = arr[i] + current_waterings
                
                if actual_height < target_h:
                    needed = target_h - actual_height
                    total_days_used += needed
                    
                    if total_days_used > k:
                        return False
                    
                    current_waterings += needed
                    if i + w < n:
                        added_height[i + w] -= needed
                        
            return total_days_used <= k

        low = min(arr)
        high = min(arr) + k
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
obj = Solution()
print(obj.maxMinHeight([2, 3, 4, 5, 1], k = 2, w = 2))