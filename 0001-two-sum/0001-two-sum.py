class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        findin = {}
        volume = len(nums)
        for i in range(volume):
            if nums[i] in findin:
                return findin[nums[i]],i
            findin[target-nums[i]] = i
            