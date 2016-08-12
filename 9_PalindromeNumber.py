class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= x <= 9:
            return True
        if x < 0:
            return False
        r = 0
        max_int32 = 2 ** 31 - 1
        temp_x = x
        while temp_x > 0:
            if r > max_int32 / 10:
                return False
            r = r * 10 + temp_x % 10
            temp_x = temp_x // 10
            if r == temp_x:
                return True

        return r == x

class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        r = 0
        while x > r:
            r = r * 10 + x % 10
            x = x // 10
        return r == x or r / 10 == x





s = Solution1()
print s.isPalindrome(0), True
print s.isPalindrome(-1), False
print s.isPalindrome(12344321), True
print s.isPalindrome(12321), True
print s.isPalindrome(1000000000003), False