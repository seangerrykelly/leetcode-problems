// https://leetcode.com/problems/array-reduce-transformation/description/?envType=study-plan-v2&envId=30-days-of-javascript
type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    var accum: number = init

    for (var i = 0; i < nums.length; i++) {
        var curr: number = nums[i]
        accum = fn(accum, curr)
    }

    return accum
};