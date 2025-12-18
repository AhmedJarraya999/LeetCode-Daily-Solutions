/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res=[]
    // return arr.map(fn);
    for (const i in arr){
        res.push(fn(arr[i],Number(i)));

    }
    return res

};