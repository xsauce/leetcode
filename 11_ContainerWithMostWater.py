class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sp = 0
        ep = len(height) - 1
        max_area = 0
        while sp < ep:
            min_val = min(height[sp], height[ep])
            temp_max_area = min_val * (ep - sp)
            max_area = max(max_area, temp_max_area)
            if min_val == height[sp]:
                sp += 1
            else:
                ep -= 1

        return max_area

class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        skip lines at both ends that don't support a higher height
        """
        sp = 0
        ep = len(height) - 1
        max_area = 0
        while sp < ep:
            min_val = min(height[sp], height[ep])
            temp_max_area = min_val * (ep - sp)
            max_area = max(max_area, temp_max_area)
            while height[sp] <= min_val and sp < ep:
                sp += 1
            while height[ep] <= min_val and sp < ep:
                ep -= 1

        return max_area


s = Solution()
print s.maxArea([10000, 2, 3, 4, 5])



