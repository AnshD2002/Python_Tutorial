#POD: Happiest Triplet
#Timestamp: 2026-02-06 04:30:17.227517

class Solution:
    def smallestDiff(self,a, b, c):
        #code here.
        a.sort()
        b.sort()
        c.sort()
        
        i = j = k = 0
        min_diff = float('inf')
        result = []
        
        while i < len(a) and j < len(b) and k < len(c):
            vals = [a[i], b[j], c[k]]
            current_min = min(vals)
            current_max = max(vals)
            current_diff = current_max - current_min
            
            if current_diff < min_diff:
                min_diff = current_diff
                result = vals
                
            if a[i] == current_min:
                i += 1
            elif b[j] == current_min:
                j += 1
            else:
                k += 1
                
        return sorted(result, reverse=True)


obj = Solution()
print(obj.smallestDiff([5, 2, 8] , [10, 7, 12] , [9, 14, 6]))