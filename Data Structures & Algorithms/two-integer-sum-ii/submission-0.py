class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 不能用兩次，兩數不能相同
        
        numbers = sorted(numbers)
        dic = {}
        for i,num in enumerate(numbers):
            minor = target - num  
            if minor not in dic:
                dic[num] = i
            else:
                if dic[minor] == i-1 and minor==num:
                    continue
                else: 
                    return [dic[minor]+1,i+1]
        return []