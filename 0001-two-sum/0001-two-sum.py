class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                return store[nums[i]],i
            else:
                store[target - nums[i]] =i
        
        