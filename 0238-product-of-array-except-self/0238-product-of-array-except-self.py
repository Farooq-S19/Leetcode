class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =len(nums)
        output =[1]*n
        for i in range(1,n):
            output[i]=nums[i-1]*output[i-1]
        sufix = 1
        for i in range(n-2,-1,-1):
            sufix = sufix *nums[i+1]
            output[i] = sufix * output[i]
        return output