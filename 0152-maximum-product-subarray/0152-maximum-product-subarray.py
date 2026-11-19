class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product =float('-inf')
        sufix=1
        prefix=1
        n =len(nums)
        for i in range(0,n):
            if prefix ==0:
                prefix=1
            prefix = prefix*nums[i]
            product=max(product,prefix)
            if sufix==0:
                sufix=1
            sufix=sufix*nums[n-i-1]
            product=max(product,sufix)
        return product