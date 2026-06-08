
class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        if x == 0:
            return 0
        base = 1
        while (base * base) <= x:
            base += 0.1
        return int(base)
    

print(Solution.mySqrt(2147395599))
