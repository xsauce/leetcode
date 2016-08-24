class Solution(object):
    MAPPING = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ''
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        self.letter_print(digits, '', result)
        return result

    def letter_print(self, digits, suffix, result):
        if digits == '':
            return
        i = 0
        while self.MAPPING[digits[i]] == '':
            i += 1
        for c in self.MAPPING[digits[i]]:
            if len(digits) == 1:
                result.append(suffix + c)
            else:
                self.letter_print(digits[i + 1:], suffix + c, result)


s = Solution()
print s.letterCombinations('')