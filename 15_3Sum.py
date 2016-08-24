class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        len_nums = len(nums)
        nums = sorted(nums)
        for i in range(len_nums - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            sp = i + 1
            ep = len_nums - 1
            while sp < ep:
                s = nums[sp] + nums[i] + nums[ep]
                if s == 0:
                    result.append([nums[i], nums[sp], nums[ep]])
                    sp += 1
                    ep -= 1
                    while sp < ep and nums[ep] == nums[ep + 1]:
                        ep -= 1
                    while sp < ep and nums[sp] == nums[sp - 1]:
                        sp += 1
                elif s > 0:
                    ep -= 1
                    while sp < ep and nums[ep] == nums[ep + 1]:
                        ep -= 1
                elif s < 0:
                    sp += 1
                    while sp < ep and nums[sp] == nums[sp - 1]:
                        sp += 1

        return result

s = Solution()
s.threeSum([-1,0,1,2,-1,-4])


def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums, L, res = sorted(nums), len(nums), []
    for i in range(L - 2):
        # if ith element is the same as i-1th element (say, -1). because -1 has been processed and no duplcate
        # allowed. So we just continue (skip this element.)
        if nums[i] == nums[i - 1] and i != 0:
            continue
        num = nums[i]
        # left and right pointer
        left, right = i + 1, L - 1

        while left < right:
            total = nums[left] + nums[right] + num

            if total == 0:
                # record result.
                res.append([nums[left], nums[right], num])
                left += 1
                right -= 1
                # skip all duplicate element.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total > 0:
                # because total is too big, we need to decrease one element of all 3. And because nums is sorted, only right should be decreased
                right -= 1
                # skip all duplicate element.
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                # same as above.
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return res
