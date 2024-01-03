function solution(n) {
    let answer = '';
    let arr = [...n.toString()];
    
    arr.sort((a, b) => b - a);
    
    for (num of arr) {
        answer += num;
    }
    
    return Number(answer);
}