function solution(x, n) {
    var answer = [];
    
    let tmp = x;
    
    while(n > 0) {
        answer.push(x);
        x += tmp;
        n -= 1;
    }
    
    return answer;
}