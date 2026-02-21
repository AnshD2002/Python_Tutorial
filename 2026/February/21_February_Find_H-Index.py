#POD: Find H-Index
#Timestamp: 2026-02-21 00:09:21.477978


class Solution:
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        
        papers_count = 0
        for i in range(n, -1, -1):
            papers_count += buckets[i]
            if papers_count >= i:
                return i
                
        return 0
    

obj = Solution()
print(obj.hIndex([3, 0, 6, 1, 5]))  # Output: 3