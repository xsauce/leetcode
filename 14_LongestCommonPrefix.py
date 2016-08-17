class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        p = 0
        shortest_len = min([len(s) for s in strs])
        while p < shortest_len:
            temp_char = strs[0][p]
            for s in strs:
                if s[p] != temp_char:
                    return s[:p]
            else:
                p += 1
        return strs[0][:shortest_len]