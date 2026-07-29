class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if i == len(nums):
                return
            j = i+1
            if nums[i] == nums[j]:
                return nums[i]