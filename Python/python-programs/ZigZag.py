
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        word_lis = [[] for _ in range(numRows)]
        rev = False
        curr_row = 0

        for each in s:
            word_lis[curr_row].append(each)

            # print(curr_row)

            if not rev and curr_row == (numRows - 1):
                rev = True
            if rev and curr_row == 0:
                rev = False
            
            if not rev:
                curr_row += 1
            else:
                curr_row -= 1
        
        res = ""
        for words in word_lis:
            for word in words:
                res += word
        
        return res

sol = Solution()

s = "PAYPALISHIRING"
print(sol.convert(s, 3))