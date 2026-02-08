#POD: Maximum Product Subarray
#Timestamp: 2026-02-08 03:31:47.149343

# LOGIC: Shrink down the array and calculate the product of the subarray. If the product is greater than the max, update the max.
class Solution:
	def arr_product(self,narr):
		for i in narr:
			self.prod = self.prod*i
			if self.max <= self.prod:
				self.max = self.prod
	def maxProduct(self,arr):
		# code here
		self.max = 0
		for i in range(len(arr)):
			for j in range(i, len(arr)):
				# print("i",i,"j",j)
				self.prod = 1
				narr = arr[i:-j]
				if i ==0 and j == 0:
					narr = arr
				# print("narr",narr)
				if 0 in narr:
					continue
				self.arr_product(narr)
				# print("max",self.max,"prod",self.prod)
				# print("next \n\n")
		return self.max
		
class OptimizedSolution:
    def maxProduct(self, arr):
        if not arr:
            return 0

        res = max_so_far = min_so_far = arr[0]

        for i in range(1, len(arr)):
            curr = arr[i]
            
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)

            res = max(res, max_so_far)

        return res
	
obj1 = OptimizedSolution()
print(obj1.maxProduct([-2, 6, -3, -10, 0, 2])) #180
print(obj1.maxProduct([2, 3, 4])) #24
obj = Solution()
print(obj.maxProduct([-2, 6, -3, -10, 0, 2])) #180
print(obj.maxProduct([2, 3, 4])) #24