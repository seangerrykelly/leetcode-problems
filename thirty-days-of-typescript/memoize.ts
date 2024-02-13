// https://leetcode.com/problems/memoize/description/?envType=study-plan-v2&envId=30-days-of-javascript
type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    let functionMap = new Map<Fn, Map<string, number>>()

    return function(...args) {
        const argKey = JSON.stringify(args)
        if (!functionMap.has(fn)) {
            functionMap.set(fn, new Map<string, number>())
            functionMap.get(fn).set(argKey, fn(...args))
        } else if (!functionMap.get(fn).has(argKey)) {
            functionMap.get(fn).set(argKey, fn(...args))
        }
        return functionMap.get(fn).get(argKey)
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */