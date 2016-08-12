def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest_num = 0
    hash_set = dict()
    sp = 0
    for ep, c in enumerate(s):
        if c in hash_set:
            longest_num = max(longest_num, ep - sp)
            sp = max(sp, hash_set[c] + 1)
        hash_set[c] = ep
    return max(longest_num, len(s) - sp)

if __name__ == '__main__':
    print lengthOfLongestSubstring('dvdf'), 3
    print lengthOfLongestSubstring('abcdef'), 6
    print lengthOfLongestSubstring('c'), 1
    print lengthOfLongestSubstring('bbbb'), 1
    print lengthOfLongestSubstring('abcabcbb'), 3
    print lengthOfLongestSubstring('pwwkew'), 3
    print lengthOfLongestSubstring('yyxxyy'), 2
    print lengthOfLongestSubstring('abcdefgxhksss'), 11
    print lengthOfLongestSubstring('aaabcdef'), 6

