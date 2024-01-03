function solution(n) {
    let tmp = n.toString(3);
    
    let tmp2 = tmp.split("").reverse().join("")
    
    return parseInt(tmp2, 3);
}