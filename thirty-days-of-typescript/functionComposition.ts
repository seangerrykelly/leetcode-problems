// https://leetcode.com/problems/function-composition/description/?envType=study-plan-v2&envId=30-days-of-javascript
type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        for (var i = functions.length - 1; i >= 0; i--) {
            x = functions[i](x)
        }
        return x
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */