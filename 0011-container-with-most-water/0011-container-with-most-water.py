class Solution:
    def maxArea(self, height: List[int]) -> int:
        storage = 0
        l =0
        r=len(height)-1
        while l<r:
            stored = min(height[l],height[r])*(r-l)
            storage = max(storage,stored)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return storage