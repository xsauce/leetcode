class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        if len(set(s)) == len(s):
            return s

        left = right = max_right = max_left = i = 0
        max_len = 1
        while i < len(s) and len(s) - i > (max_len / 2):
            left = right = i
            while right < len(s) - 1 and s[right] == s[right + 1]:
                right += 1
            i = right + 1
            while right < len(s) - 1 and left > 0 and s[right + 1] == s[left - 1]:
                left -= 1
                right += 1
            new_len = right - left + 1
            if max_len < new_len:
                max_left = left
                max_right = right
                max_len = new_len
        return s[max_left: max_right + 1]

print Solution().longestPalindrome('bab'), 'bab'
print Solution().longestPalindrome('xxyyzzbab'), 'bab'
print Solution().longestPalindrome('aaaa'), 'aaaa'
print Solution().longestPalindrome('babzzxx'), 'bab'
print Solution().longestPalindrome('bababccba'), 'abccba'