class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        val = 0
        while x>0:
            val = (val*10)+(x%10)
            x=x//10
        return val == temp
