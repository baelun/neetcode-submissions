class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i]代表後幾天溫度會比當下溫度高

        # lens = len(temperatures)
        # result = [0] * lens 
        # for l in range(lens):
        #     for r in range(l,lens):
        #         if temperatures[r] > temperatures[l]:
        #             result[l] = r-l
        #             break  
                
        # return result
        
        lens = len(temperatures)
        stack = []
        result = [0] * lens
        for i in range(lens):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_index = stack.pop()
                result[pre_index] = i - pre_index
            
            stack.append(i)
        return result
        
