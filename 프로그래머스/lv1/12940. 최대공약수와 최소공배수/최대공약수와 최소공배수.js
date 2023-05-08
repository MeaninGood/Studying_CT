function solution(n, m) {
    var answer = [];
    
    let a = n, b = m;
    if(m > n) a = m, b = n;
    
    console.log(a, b);
    
    while(b != 0) {
        let tmp = a;
        a = b;
        b = tmp % b;
    }
    
    answer = [a, n * m / a];
    
    return answer;
}