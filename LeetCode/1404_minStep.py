class Solution:
    @staticmethod
    def numSteps(self, s: str) -> int:
        # convert a binary number to denary
        based = 1
        denary = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                denary += based

            based *= 2
        
        print(denary)

        count = 0
        while denary != 1:
            # If odd, add 1
            if denary % 2 != 0:
                denary += 1
            # Else even
            else:
                denary = int(denary / 2)
            count += 1
        
        print(count)
        return count

Solution.numSteps("1")