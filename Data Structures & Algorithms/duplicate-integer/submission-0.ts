class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const dup: any = {}

        for (let num of nums) {
            if (dup[num] >= 1) {
               return true
            }
            dup[num] = 1
        }
        return false
    }
}
