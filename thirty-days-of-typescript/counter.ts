// https://leetcode.com/problems/counter/description/
function createCounter(n: number): () => number {
    var callCount: number = 0;
    return function() {
        const result: number = n + callCount;
        callCount += 1
        return result;
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */