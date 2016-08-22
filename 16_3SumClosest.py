class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        nums = sorted(nums)
        found = None
        for i in range(len_nums - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            sp = i + 1
            ep = len_nums - 1
            while sp < ep:
                s = nums[sp] + nums[i] + nums[ep]
                if s == target:
                    return target
                elif s > target:
                    if found is None or (abs(s - target) < abs(found - target)):
                        found = s
                    ep -= 1
                    while sp < ep and nums[ep] == nums[ep + 1]:
                        ep -= 1
                elif s < target:
                    if found is None or (abs(s - target) < abs(found - target)):
                        found = s
                    sp += 1
                    while sp < ep and nums[sp] == nums[sp - 1]:
                        sp += 1
        return found


s = Solution()
print s.threeSumClosest([0,2,1,-3], 1)