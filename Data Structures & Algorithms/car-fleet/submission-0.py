class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 車子不能超過它前面的車
        # 車隊是一個非空的每台車在同一個位置與速度，一台車業可以被視為是車隊
        # 如果車子到了車隊 某個瞬間抵達了目的地，車子就會被視為是車隊的一部份
        # 回傳不同車隊的數目
        stack = []
        # time = (target-postition)/speed
        car = sorted(zip(position,speed),reverse = True) 
        for pos, spd in car:
            cur_time = (target - pos)/spd
            if not stack or cur_time > stack[-1]:
                stack.append(cur_time)
        return len(stack)