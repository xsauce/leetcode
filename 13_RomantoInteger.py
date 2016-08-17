class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        pre = None
        r = 0
        for i in s[::-1]:
            if pre and ROMAN[pre] > ROMAN[i]:
                signal = -1
            else:
                signal = 1
            r += signal * ROMAN[i]
            pre = i
        return r

s = Solution()
print s.romanToInt('III'), 3
print s.romanToInt('CIV'), 104
print s.romanToInt('MCMLIV'), 1954
