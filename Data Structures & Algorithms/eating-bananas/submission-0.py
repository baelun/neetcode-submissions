class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 每小時吃的數量等於nums/k，可選擇一坨香蕉吃掉k個香蕉
        # 如果那陀香蕉數量小於 k ，就需要吃掉那陀香蕉，
        # 回傳最小k讓我可以吃掉所有香蕉在h小時裡。
        # 如果 K 個吃大於h則減少k
        # 如果 k 個吃小於h則增加k

        def caculate(k):
            result = 0    
            for pile in piles:
                if k >= pile:
                    result += 1
                else:
                    result += (pile + k - 1)//k  # 考慮了整除與非整除算法
            return result

        l = 1
        r = max(piles)  
        ## 紀錄最小可行速度
        ans = r
        while l <= r:
            mid = (l+r)//2
            result = caculate(mid)
            if result <= h:  # k越大花費時數越少，速度可以放慢(因為要取最小速度)
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
