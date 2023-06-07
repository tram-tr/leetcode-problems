/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashMap = new Map();
    const res = [0,0];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in hashMap) {
            res[0] = hashMap[nums[i]];
            res[1] = i;
        }
        hashMap[target - nums[i]] = i;
    }

    return res;
};
