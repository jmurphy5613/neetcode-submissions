class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        maxVal = float('inf')
        if nums[l] < nums[r]:
            return nums[0]
        while l <= r:
            m = r+l // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
            maxVal = min(maxVal, nums[m])
        return maxVal
        
        

        