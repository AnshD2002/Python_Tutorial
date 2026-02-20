#POD: Form the Largest Number
#Timestamp: 2026-02-20 23:03:34.053655

from functools import cmp_to_key

class Solution:
        def findLargest(self, arr):
            arr = list(map(str, arr))
            def compare(x, y):
                if x + y > y + x:
                    return -1
                else:
                    return 1
            arr.sort(key=cmp_to_key(compare))
            result = "".join(arr)
            return "0" if result[0] == "0" else result

obj = Solution()
arr = [3, 30, 34, 5, 9]
print(obj.findLargest(arr))