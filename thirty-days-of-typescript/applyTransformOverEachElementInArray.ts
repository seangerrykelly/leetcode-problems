// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/?envType=study-plan-v2&envId=30-days-of-javascript
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    arr.forEach((n, i) => {
        arr[i] = fn(n, i)
    })
    return arr
};