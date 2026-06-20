class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        # 如果後面有高度低於stack裡面的長度，先算出當下的面積，更新最大面積
        # 把之前的最小Index彈出，放入目前最小index
        heights.append(0)
        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                pre_index = stack[-1]

                if len(stack)==1: # 前面的都比他小，
                    w = i 
                else:
                    w = i - stack[-2] - 1
                cur_area = w * heights[pre_index]
                max_area = max(max_area,cur_area)
                stack.pop()
               
            
            stack.append(i)

        return max_area
