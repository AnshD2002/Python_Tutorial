#POD: Sum of subarray ranges
#Timestamp: 2026-01-22 18:29:15.725513

class Solution:
    def subarrayRanges(arr):
        # Code here
        sol = 0
        for i in arr:
            print("i =", i )
            for j in arr:
                print("j =", j )
                if i >= j:
                    print(i ," + ",j)
                    sol = sol+(i-j)
        return sol
        
obj = Solution
print(Solution.subarrayRanges(arr=[-32, 0, -2, 72]))