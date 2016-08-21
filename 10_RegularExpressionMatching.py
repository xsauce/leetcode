__author__ = 'samgu'
class Solution(object):
    '''
    time out
    "aaaaaaaaaaaaab"
    "a*a*a*a*a*a*a*a*a*a*c"
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (s != '' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            return s != '' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])




s = Solution()
print 1, s.isMatch("aa","a"), False
print 2, s.isMatch("aa","aa"), True
print 3, s.isMatch("aaa","aa"), False
print 4, s.isMatch("aa", "a*"), True
print 5, s.isMatch("aa", ".*"), True
print 6, s.isMatch("ab", ".*"), True
print 7, s.isMatch("aab", "c*a*b"), True
print 8, s.isMatch("abb", "a*b*"), True
print 9, s.isMatch('1a2b3c', ".a.b.c"), True
print 10, s.isMatch('a1b', 'c*a.b*c*d*'), True
print 11, s.isMatch('a1b', 'c*a.b*c*d'), False
print 12, s.isMatch('aaa', 'a*a'), True
print 13, s.isMatch('', '.'), False
print 14, s.isMatch('ab', 'c*a*c*b'), True
print 15, s.isMatch('aaa', 'aaaa'), False
print 16, s.isMatch('aaa', 'ab*a*c*a'), True


