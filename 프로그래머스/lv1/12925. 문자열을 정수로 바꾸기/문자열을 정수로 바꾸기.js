function solution(s) {
    
    const arr = [...s];

    let answer = arr[0] === '+' | arr[0] === '-' ? arr.shift() : '';
    
    for(num of arr) {
        answer += num;
    }
  
    return Number(answer);
}