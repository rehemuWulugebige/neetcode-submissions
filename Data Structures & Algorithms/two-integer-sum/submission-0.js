class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = {}
        for(let i = 0; i < nums.length; i++) {
            let diff = target - nums[i]
            if (map[diff] !== undefined) {
                return [map[diff], i]
            }else {
                map[nums[i]] = i
            }
        }
        return []
    }
}

// const test = new Solution()
// console.log(test.twoSum([3, 4, 5, 6], 7))
