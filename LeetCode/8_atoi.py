class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        # get rid of the leading white space
        s = s.strip()

        # edge case where s = ""
        if s == "":
            return 0

        # determine the sign
        is_neg = False
        if s[0] == '-':
            s = s[1:]
            is_neg = True
        elif s[0] == '+':
            s = s[1:]
        
        print(s)

        # Read the integer
        res = ""
        is_digit = False
        for each in s:
            if each.isdigit():
                is_digit = True
                res += each
            else:
                is_digit = False

            if not is_digit:
                break

        if res == "":
            res = "0"

        res_num = int(res)

        # Rounding
        if res_num >= 2**(31) - 1 and not is_neg:
            res_num = 2**(31) - 1
        if -res_num <= - 2**(31):
            res_num = 2**(31)

        return res_num if not is_neg else -res_num

print(Solution.myAtoi("-+12"))