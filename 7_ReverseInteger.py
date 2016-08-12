class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        signal = 1 if x > 0 else -1
        x = signal * x
        r = 0
        while x > 0:
            r = r * 10 + (x % 10)
            x = x // 10
        r *= signal
        if r < -2147483648 or r > 2147483647:
            return 0
        return r