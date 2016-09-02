class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        L = len(nums)
        l = 0
        r = L - 1
        nums = sorted(nums)
        # add check
        while l < r and (nums[l] + 3 * nums[r] < target):
            l += 1
        while l < r and (3 * nums[l] + nums[r] > target):
            r -= 1
        #
        for i in range(l, r - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, L - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = L - 1
                num2 = nums[i]
                num1 = nums[j]
                while left < right:
                    s = nums[left] + num1 + num2 + nums[right]
                    if s == target:
                        r = [num1, num2, nums[left], nums[right]]
                        result.append(r)
                        left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif s > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result

    def nSum(self, nums, start, n, target):
        result = []
        L = len(nums)
        if L == 0:
            return result
        if n * nums[start] > target or n * nums[L - 1] < target:
            return result
        for i in range(start, L - n + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if n == 1:
                if nums[i] < target:
                    continue
                elif nums[i] > target:
                    break
                else:
                    result = [[target]]
            else:
                for iresult in self.nSum(nums, i + 1, n - 1, target - nums[i]):
                    iresult.append(nums[i])
                    result.append(iresult)
        return result

    def fourSum_rev(self, nums, target):
        return self.nSum(sorted(nums), 0, 4, target)



s = Solution()
print s.fourSum_rev([], 0)
