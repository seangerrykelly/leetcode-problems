// https://leetcode.com/problems/array-wrapper/description/?envType=study-plan-v2&envId=30-days-of-javascript
class ArrayWrapper {
    
    nums: number[] = []
    sum: number = 0
    str: string = '[]'

    constructor(nums: number[]) {
        this.nums = nums
    }
    
    valueOf(): number {
        for (var i = 0; i < this.nums.length; i++) {
            const curr = this.nums[i]
            this.sum += curr
        }
        return this.sum
    }
    
    toString(): string {
        if (this.nums.length > 0) {
            this.str = ''
        }
        for (var i = 0; i < this.nums.length; i++) {
            const curr = this.nums[i]
            if (i == 0) {
                // First iteration
                this.str += '[' + curr + ','
            } else if (i < this.nums.length - 1) {
                // Intermediate iterations
                this.str += curr + ','
            } else {
                // Final iteration
                this.str += curr + ']'
            }
        }
        return this.str
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */