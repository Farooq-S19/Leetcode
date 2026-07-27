class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)

        def slove(n: int)-> int:
            if n<=2:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n] = slove(n-1)+ slove(n-2)
            return dp[n]
        return slove(n)