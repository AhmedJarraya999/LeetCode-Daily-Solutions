/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let accsum=init
    for (const i in nums){
        accsum=fn(accsum,nums[i])
    }
    return accsum
    
    
};