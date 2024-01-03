function solution(a, b, n) {
    var answer = 0;
    
    let x = n, y = 0;
    while(true) {
        
        y = x % a;
        x = b * Math.floor(x / a);
        answer += x;
        
        if(x + y < a) return answer;
        
        x = x + y;
        y = 0;
        
        
    }
    return answer;
}