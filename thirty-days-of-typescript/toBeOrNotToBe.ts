// https://leetcode.com/problems/to-be-or-not-to-be/submissions/1169088483/?envType=study-plan-v2&envId=30-days-of-javascript
type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    const toBe = (otherVal: any): boolean => {
        if (val === otherVal) {
            return true
        } else {
            throw Error("Not Equal")
        }
    }

    const notToBe = (otherVal: any): boolean => {
        if (val !== otherVal) {
            return true
        } else {
            throw Error("Equal")
        }
    }

    return { toBe, notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */