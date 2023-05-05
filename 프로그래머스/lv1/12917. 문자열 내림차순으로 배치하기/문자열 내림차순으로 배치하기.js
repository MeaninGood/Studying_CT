function solution(s) {
    const arr = [...s];
    
    var answer = '';
    
    arr.sort();
    
    for(let i = arr.length - 1; i >= 0; i--) {
        answer += arr[i];
    }
    
    return answer;
}