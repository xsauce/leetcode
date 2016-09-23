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
        if n == 2:
            return ['(())', '()()']
        if n == 1:
            return ['()']
        result = set()
        child_results = {}
        for i in range(1, n):
            i_temp_child_result = child_results.get(i, None)
            n_i_temp_child_result = child_results.get(n - i, None)
            if i_temp_child_result is None:
                child_results[i] = self.generateParenthesis(i)
            if n_i_temp_child_result is None:
                child_results[n - i] = self.generateParenthesis(n - i)

            for j in child_results[i]:
                result.add(j + (n - i) * '(' + (n - i) * ')')
            for j in child_results[n - i]:
                result.add(i * '(' + ')' * i + j)
        result.add(n * '(' + ')' * n)
        return list(result)

s = Solution()
for i in sorted(s.generateParenthesis(5)):
    print i


