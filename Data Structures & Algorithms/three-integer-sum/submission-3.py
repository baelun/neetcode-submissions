class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        lens = len(nums)
        nums = sorted(nums)
        set_ = set()
        for i in range(lens-2):
            l,r = i+1,lens-1
            while l<r:
                val = nums[i]+nums[l]+nums[r]
                if val == 0 :
                    set_.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif val<0:
                    l+=1
                else:
                    r-=1

        return list(set_)