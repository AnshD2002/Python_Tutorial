#POD: Count Subarrays with given XOR
#Timestamp: 2026-02-22 22:06:44.794268

from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        res = 0
        prefix_xor = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        for num in arr:
            prefix_xor ^= num
            target = prefix_xor ^ k
            res += count_map[target]
            count_map[prefix_xor] += 1
            
        return res


obj = Solution()
print(obj.subarrayXor(arr = [4, 2, 2, 6, 4], k = 6))
