class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = 0
        signal = 1
        flag = 0
        for c in str:
            if c == ' ' and flag == 0:
                continue
            if c == '+' and flag == 0:
                signal = 1
                flag = 1
                continue
            if c == '-' and flag == 0:
                signal = -1
                flag = 1
                continue
            if ord(c) < 48 or ord(c) > 57:
                break
            else:
                r = r * 10 + (ord(c) - 48)
                flag = 1

        r *= signal
        if r < -2 ** 31:
            r = -2 ** 31
        if r > 2 ** 31 - 1:
            r = 2 ** 31 - 1
        return r


s = Solution()

print s.myAtoi(''), 0
print s.myAtoi('123'), 123
print s.myAtoi('-123'), -123
print s.myAtoi('  '), 0
print s.myAtoi('  0123000 '), 123000
print s.myAtoi('  -0123 '), -123
print s.myAtoi(' 123abc'), 123
print s.myAtoi(' -123abc'), -123
print s.myAtoi('abc123'), 0
print s.myAtoi('abc-123'), 0
print s.myAtoi('2147483648'), 2147483647
print s.myAtoi('-2147483649'), 2147483648
print s.myAtoi('  +11bc11'), 11
print s.myAtoi('  -bc123'), 0
print s.myAtoi('  +-2'), 0
print s.myAtoi("   +0 123"), 0
print s.myAtoi("123 456"), 123