// https://leetcode.com/problems/sort-by/description/?envType=study-plan-v2&envId=30-days-of-javascript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (value: JSONValue) => number

function quickSort(arr: JSONValue[], fn: Fn) {
    if (arr.length <= 1) {
        return arr
    }
    const pivot = arr.pop()
    const pivotComparator = fn(pivot)
    let lower = []
    let greater = []
    for (var i = 0; i < arr.length; i++) {
        const curr = arr[i]
        const comparator = fn(arr[i])
        if (comparator <= pivotComparator) {
            lower.push(curr)
        } else {
            greater.push(curr)
        }
    }
    var sortedArr = []
    return sortedArr.concat(quickSort(lower, fn), [pivot], quickSort(greater, fn))
}

function sortBy(arr: JSONValue[], fn: Fn): JSONValue[] {
    return quickSort(arr, fn)
};