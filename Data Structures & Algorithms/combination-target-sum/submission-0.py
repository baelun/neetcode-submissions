class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        combination = []
        def back(start,path,current_val):
            if current_val == 0:
                combination.append(list(path)) 
                return
            if current_val < 0:
                return 
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                back(i,path,current_val-nums[i])
                path.pop()

        back(0,[],target)
        return combination