// https://leetcode.com/problems/join-two-arrays-by-id/description/?envType=study-plan-v2&envId=30-days-of-javascript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function buildMap(arr: ArrayType[], idMap: Map<number, Map<string, JSONValue>>) {
    arr.forEach((item) => {
        if (!idMap.get(item['id'])) {
            idMap.set(item['id'], new Map<string, JSONValue>())
        }
        for (var key in item) {
            if (key == 'id') {
                continue
            } else {
                idMap.get(item['id']).set(key, item[key])
            }
        }
    })
    return idMap
}

function quickSort(arr: ArrayType[]): ArrayType[] {
    if (arr.length <= 1) {
        return arr
    }
    const pivot = arr.pop()
    let lower = []
    let greater = []

    arr.forEach((item) => {
        if (item['id'] <= pivot['id']) {
            lower.push(item)
        } else {
            greater.push(item)
        }
    })
    return [].concat(quickSort(lower), [pivot], quickSort(greater))
}

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    let result: ArrayType[] = []
    let idMap = new Map<number, Map<string, JSONValue>>()
    idMap = buildMap(arr1, idMap)
    idMap = buildMap(arr2, idMap)

    idMap.forEach((value, key) => {
        let json: ArrayType = {"id": key}
        value.forEach((v, k) => {
            json[k] = v
        })
        result.push(json)
    })

    // Sort the result before returning
    result.sort((a, b) => {
        if (a['id'] < b['id']) {
            return -1
        } else {
            return 1
        }
    })
    return result
};