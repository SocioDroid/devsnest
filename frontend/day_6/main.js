/*
To execute the code, type 'node main.js' in console!!
*/

const is_array = val => {
    return val instanceof Array
}

console.log(is_array('w3resource'));
console.log(is_array([1, 2, 4, 0]));

const clone_array = original_array => {
    let clone = original_array.map(el => el)
    return clone
}

console.log("Cloned Array:", clone_array([1, 2, 4, 0]));
console.log("Cloned Array:", clone_array([1, 2, [4, 0]]));

const first = (arr, n = 0) => {
    if (n >=arr.length) return arr;
    else if (n == 0) return arr[n];
    ans_arr = []
    for(let i = 0; i<n; i++){
        ans_arr.push(arr[i])
    }
    return ans_arr
}

console.log("First:", first([7, 9, 0, -2]));
console.log("First:", first([],3));
console.log("First:", first([7, 9, 0, -2],3));
console.log("First:", first([7, 9, 0, -2],6));
console.log("First:", first([7, 9, 0, -2],-3));

const join_array_elements = (arr, del = "") => {
    ans_str = ""
    arr.forEach(element => {
        ans_str += element + del
    });
    if (del !== "") ans_str = ans_str.slice(0, -(del.length));
    return ans_str
}

console.log("Joined Elements:", join_array_elements(["Red", "Green", "White", "Black"],","))
console.log("Joined Elements:", join_array_elements( ["Red", "Green", "White", "Black"],"+"))

const get_max_freq = arr => {
    freq = {}
    arr.forEach(element => {
        if (freq[element] === undefined) freq[element] = 1
        else freq[element] += 1
    });
    max_f = -1
    max_key = undefined
    for(f in freq){
       if (freq[f] > max_f) {
           max_f = freq[f];
           max_key = f
        } 
    }
    return max_key
}

console.log("Max Occuring Element :", get_max_freq([3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3]))