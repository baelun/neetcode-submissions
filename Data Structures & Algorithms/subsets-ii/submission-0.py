class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        path = []
        conbination = []
        def combi(index,path):
            
            conbination.append(path[:])
            
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                combi(i+1,path)
                path.pop()
        combi(0,path)
        return conbination