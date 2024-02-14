// https://leetcode.com/problems/chunk-array/description/?envType=study-plan-v2&envId=30-days-of-javascript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    let result: Obj[][] = []
    let counter: number = size
    let chunkArr: Obj[] = []
    
    for(var i = 0; i < arr.length; i++) {
        chunkArr.push(arr[i])
        counter--
        if (counter == 0) {
            counter = size
            result.push(chunkArr)
            chunkArr = []
        } else if (i == arr.length - 1) {
            // If we are on the last iteration but final subarray is less than size
            result.push(chunkArr)
        }
    }

    return result
};
