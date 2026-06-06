class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lens = len(prices)
        max_val = 0
        for i in range(lens):
            j = i+1 
            while j<lens:
                if prices[j] > prices[i] :
                    max_val = max(max_val,prices[j] - prices[i])
                    j+=1                    
                else:
                    j+=1
                    
        return max_val