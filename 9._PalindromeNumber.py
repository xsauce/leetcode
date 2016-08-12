class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if -9 <= x <= 9:
            return x
        x = abs(x)
        while x > 0:
            x = x // 10



s = Solution()
print s.isPalindrome(0), 0