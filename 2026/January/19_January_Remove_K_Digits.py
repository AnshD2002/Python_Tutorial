#POD: Remove K Digits
#Timestamp: 2026-01-19 00:44:28.713258

class Solution:
    def removeKdig(self, s: str, k: int) -> str:
        stack = []
        for digit in s:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k > 0:
            stack = stack[:-k]
            
        result = "".join(stack).lstrip("0")
        return result if result else "0"
            



obj = Solution()
s = "1432219"
k = 3
print(obj.removeKdig(s, k))  # Output: "1219"
