class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cur = nums[math.trunc((len(nums) - 1) / 2)]
        curIndex = math.trunc((len(nums) - 1) / 2)
        curArr = nums
        numsOffset = 0
        while cur != target:
            if len(curArr) == 1:
                return -1
            if cur > target:
                if curIndex == 0:
                    return -1
                curArr = curArr[0:curIndex]
            else:
                numsOffset += len(curArr[0:curIndex+1])
                curArr = curArr[curIndex+1:len(curArr)]
            cur = curArr[math.trunc((len(curArr)-1)/2)]
            curIndex = math.trunc((len(curArr)-1)/2)
        return curIndex + numsOffset;