class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","]":"[","}":"{"}

        for i in s:
            if i in mapping:      
                if stack == []:
                    return False
                if stack != []:
                    left = stack.pop() 
                    if left != mapping[i]:
                        return False
                else:
                    continue
            else:
                stack.append(i)
        return len(stack) == 0
        