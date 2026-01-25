#POD: Generate Permutations of an array
#Timestamp: 2026-01-26 02:43:34.511291

class Solution:
    def permutations(self,res, arr, idx):
        if idx == len(arr):
            res.append(arr[:])
            return
        for i in range(idx, len(arr)):
            arr[idx], arr[i] = arr[i], arr[idx]
            self.permutations(res, arr, idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]
    def permuteDist(self,arr):
        res = []
        self.permutations(res, arr, 0)
        return res

obj = Solution()
print(obj.permuteDist([1, 2, 3]))