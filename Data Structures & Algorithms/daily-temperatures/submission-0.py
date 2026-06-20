class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i]代表後幾天溫度會比當下溫度高

        lens = len(temperatures)
        result = [0] * lens 
        for l in range(lens):
            for r in range(l,lens):
                if temperatures[r] > temperatures[l]:
                    result[l] = r-l
                    break  
                
        return result