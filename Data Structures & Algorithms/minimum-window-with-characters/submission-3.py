class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        len_t = len(t)
        l = 0
        r = 0
        count_s = Counter()
        count_t = Counter(t)
        res_len = float("inf")
        min_l, min_r = -1, -1
        have,need = 0,len(count_t)

        while r < len(s):
            count_s[s[r]] += 1
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1  #一個字元滿足
                
            while have == need:
                lens = r-l+1
                if lens < res_len:
                    res_len = lens
                    min_l,min_r = l,r
                
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]]<count_t[s[l]]:
                    have -= 1
                l += 1

            r += 1
        
        return s[min_l:min_r+1]