function solution(num) {
    var answer = 0;
    
    let tmp = num;
    let cnt = 0;
    while(true){
        if (cnt >= 500) return -1;
        
        if (tmp === 1) return cnt;
        
        if (tmp % 2) tmp = tmp * 3 + 1;
        else tmp = Math.floor(tmp / 2);
        
        cnt++;
    }
    return answer;
}