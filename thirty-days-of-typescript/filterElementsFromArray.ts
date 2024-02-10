// https://leetcode.com/problems/filter-elements-from-array/description/?envType=study-plan-v2&envId=30-days-of-javascript
type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    var result: number[] = []
    arr.forEach((item, index) => {
        if (fn(item, index)) {
            result.push(item)
        }
    })
    return result
};