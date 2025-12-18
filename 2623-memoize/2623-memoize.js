/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map(); 
    return function(...args) {
        const key = JSON.stringify(args);
        //check if in cache
        if (cache.has(key)) {
            return cache.get(key);
        }
        // Call the function and store the result in cache
        const result = fn(...args);
        cache.set(key, result);
        return result;
        
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