class Solution(object):
    def to_roman(self, num, int_num):
        if 1 <= int_num < 10:
            l, m, h = 'I', 'V', 'X'
        elif 10 <= int_num < 100:
            l, m, h = 'X', 'L', 'C'
        elif 100 <= int_num < 1000:
            l, m, h = 'C', 'D', 'M'
        else:
            l, m, h = 'M', 'M', 'M'

        if 1 <= num <= 3:
            return l * num
        elif num == 4:
            return l + m
        elif num == 5:
            return m
        elif 6 <= num <= 8:
            return m + l * (num - 5)
        elif num == 9:
            return l + h
        else:
            return ''


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = 0
        roman = ''
        while num > 0:
            x = num % 10
            roman = self.to_roman(x, x * (10 ** base)) + roman
            num = num // 10
            base += 1
        return roman

s = Solution()
print s.intToRoman(1954), 'MCMLIV'
print s.intToRoman(1900), 'MCM'