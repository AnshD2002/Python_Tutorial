class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        low = 0
        high = n - 1

        if arr[low] <= arr[high]:
            return 0

        while low <= high:
            mid = low + (high - low) // 2

            if mid < high and arr[mid + 1] < arr[mid]:
                return mid + 1

            if mid > low and arr[mid] < arr[mid - 1]:
                return mid

            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid - 1

        return 0

obj =Solution()
print(obj.findKRotation([5, 1, 2, 3, 4]))