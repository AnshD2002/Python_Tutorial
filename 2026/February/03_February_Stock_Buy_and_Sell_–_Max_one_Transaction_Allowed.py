#POD: Stock Buy and Sell � Max one Transaction Allowed
#Timestamp: 2026-02-03 14:04:06.103923

class Solution:
            
    def maxProfit(self, prices):
        # code here
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

obj = Solution()
print(obj.maxProfit(prices=[7, 10, 1, 3, 6, 9, 2]))