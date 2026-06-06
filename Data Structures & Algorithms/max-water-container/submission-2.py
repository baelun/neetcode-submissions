class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        lens = len(heights)
        l,r = 0,lens-1
        max_area = 0
        while l<r:
            val = min(heights[l],heights[r]) * (r-l)
            max_area = max(max_area,val)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            elif heights[l] == heights[r]:
                l+=1
                r-=1
        
        return max_area


            