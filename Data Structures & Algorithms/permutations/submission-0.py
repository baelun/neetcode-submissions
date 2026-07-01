class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        numset = set()
        path = []
        combi = []
        def combination(path):
            if len(path) == len(nums):
                combi.append(path[:])
            for num in nums:
                if num not in numset:    
                    path.append(num)
                    numset.add(num)
                    combination(path)
                    path.pop()
                    numset.remove(num)
        combination(path)
        return combi