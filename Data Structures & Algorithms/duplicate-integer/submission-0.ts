class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const uniqueNums = new Set<number>()
        for (const num of nums) {
            if (uniqueNums.has(num)) return true
            uniqueNums.add(num)
        }
        return false
    }
}
