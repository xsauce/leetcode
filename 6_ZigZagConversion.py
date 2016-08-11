class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s
        r = []
        for i in range(numRows):
            r += self.print_one_line(s, numRows, i)
        return ''.join(r)

    def print_one_line(self, s, numRows, row_index):
        is_down = 1
        cur = row_index
        r = []
        while cur < len(s):
            r.append(s[cur])
            if row_index == numRows - 1 or row_index == 0:
                temp_num_rows = numRows
            else:
                if is_down == 1:
                    temp_num_rows = numRows - row_index
                else:
                    temp_num_rows = row_index + 1
            is_down = -1 * is_down
            cur += temp_num_rows * 2 - 2
        return r


# print Solution().convert('012345', 3), '041352'
# print Solution().convert(''.join('0123456789abcdef'), 5), ''
print Solution().convert('A', 1)
print Solution().convert('AB', 1)


class Solution1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # initialize a matrix with numRows * empty strings
        matrix = [""]*numRows
        # default moving direction, down
        inc = 1
        # i is the index of row in the matrix
        i = 0
        for x in range(len(s)):
            # append char in s to corresponding row of matrix
            matrix[i] += s[x]
            # if out of boundary, change moving direction
            if i+inc >=numRows or i+inc < 0:
                inc = -inc
            i += inc
        # append each strings in matrix to the result string
        res = ''.join(matrix)
        return res
