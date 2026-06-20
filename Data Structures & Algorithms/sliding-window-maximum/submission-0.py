class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_window = []

        l = 0
        
        
        for l in range(len(nums)-k+1):
            r = l + k -1
            max_num = max(nums[l:r+1])
            max_window.append(max_num)

        return max_window
            