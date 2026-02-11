#POD: Equalize the Towers
#Timestamp: 2026-02-11 23:44:52.707435

class Solution:
    def minCost(self, heights, cost):
        #code here
        def get_total_cost(h):
            res = 0
            for i in range(len(heights)):
                res += abs(heights[i] - h) * cost[i]
            return res

        low = min(heights)
        high = max(heights)
        ans = get_total_cost(low)

        while low <= high:
            m1 = low + (high - low) // 3
            m2 = high - (high - low) // 3
            
            c1 = get_total_cost(m1)
            c2 = get_total_cost(m2)
            
            ans = min(ans, c1, c2)
            
            if c1 < c2:
                high = m2 - 1
            else:
                low = m1 + 1
                
        return ans
    
# Example usage:
solution = Solution()
heights = [1, 2, 3]
cost = [10, 100, 1000]
print(solution.minCost(heights, cost))  # Output: 120