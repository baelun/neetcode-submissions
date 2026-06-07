class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lens = len(s)
        l = 0
        char_set = set()
        m_len = 0
    
        for r in range(lens): 
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            m_len = max(m_len,r-l+1)
            
                
        return m_len
