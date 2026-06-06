class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome是從往後或從後往前都是一樣的字就是true
        
        string = []
        s = s.lower()
        lens = 0
        for char in s :
            if char.isalnum():  
                string.append(char)
                lens+=1
        l,r = 0,lens-1
        while l<=r:
            if string[l]!=string[r]:
                return False
            if string[l] == string[r]:
                l+=1
                r-=1
                continue

        return True
                