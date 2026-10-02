class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        rotations = 0
        while nums[l] > nums[r]:
            l += 1
        l -= 1
        rotatedArr = nums[0:l]
        rotatedArr = nums[l+1:r+1] + rotatedArr
        return rotatedArr[0]

        

        