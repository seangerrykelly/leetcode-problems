// https://leetcode.com/problems/counter-ii/description/
type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    var currentCount: number = init;

    function increment() {
        currentCount += 1;
        return currentCount;
    }

    function decrement() {
        currentCount -= 1;
        return currentCount;
    }

    function reset() {
        currentCount = init;
        return currentCount;
    }

    return { increment, decrement, reset }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */