function solution(prices) {
    const n = prices.length;
    
    const arr = Array(prices.length).fill(0);
    
    for (let i = 0; i <= n - 2; i++) {
        let cnt = 0;
        let idx = prices[i];
        
        for (let j = i + 1; j <= n - 1; j++) {
            if (idx > prices[j]) {
                cnt++;
                break;
            }
            cnt++;
        }
        
        arr[i] = cnt;
    }
    
    return arr;
}