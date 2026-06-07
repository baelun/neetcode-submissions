class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 選定一個字母變換，得到最大長度的相同字母的substr長度
        lens = len(s)
        
        max_lens = 0
  
        char_set= set(s)

        for char_ in char_set:
            count = 0
            l = 0
            for r in range(lens):   
                if s[r] == char_:
                    count += 1
                while (r-l+1) - count > k:
                    if s[l] == char_:
                        count -= 1
                    l+=1  #讓他繼續跑下個r 
                max_lens = max(max_lens,r-l+1)
        
        return max_lens
                    
            
                    
  
            
        
        