class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        lens_s2 = len(s2)
        s1_counter = Counter(s1)
        s2_counter = Counter()
        l = 0
        r = 0
        while r < lens_s2:
            s2_counter[s2[r]] += 1
            if r-l+1 == len(s1):
                if s1_counter == s2_counter:
                    return True
                else:
                    s2_counter[s2[l]]-=1
                    if s2_counter[s2[l]] == 0:
                        del s2_counter[s2[l]]
                l+=1
            r+=1
        return False
       