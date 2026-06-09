class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #往中間搜索，假如l>r然後l>mid>target往右，如果l>target>mid 往左
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            if nums[mid] > nums[r]:   #如果中間值大於右邊，左半邊就是遞增
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1