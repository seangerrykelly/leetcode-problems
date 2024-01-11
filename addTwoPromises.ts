// https://leetcode.com/problems/add-two-promises/description/
type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    const number1 = await promise1.then((value) => {
        return value;
    });
    const number2 = await promise2.then((value) => {
        return value
    });
    const sum = number1 + number2
    return Promise.resolve(sum)
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */