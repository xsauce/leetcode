# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        situations = set()
        self.list_all_add_situation(n, situations)
        situations.add([n, 0])
        for i in situations:
            print i

    def list_all_add_situation(self, n):
        if n == 1:
            return [1]
        child_result = []
        if n % 2 == 0:
            child_n = n // 2
            situations.add((child_n, child_n))
            situations.add(([child_n] + self.list_all_add_situation(child_n, situations)))
            situations.add((self.list_all_add_situation(child_n, situations) + [child_n]))
        else:
            small_child_n = n // 2
            big_child_n = n // 2 + 1
            situations.add((small_child_n, big_child_n))
            situations.add(([small_child_n] + self.list_all_add_situation(big_child_n, situations)))
            situations.add((self.list_all_add_situation(small_child_n, situations) + [big_child_n]))

            situations.add((big_child_n, small_child_n))
            situations.add(([big_child_n] + self.list_all_add_situation(small_child_n, situations)))
            situations.add((self.list_all_add_situation(big_child_n, situations) + [small_child_n]))

s = Solution()
s.generateParenthesis(5)



