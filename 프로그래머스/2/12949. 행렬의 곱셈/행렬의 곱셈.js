function solution(arr1, arr2) {
    let answer = [];
    
    const n = arr1.length;
    const m = arr2[0].length;
    const t = arr2.length;
    
    for (let i = 0; i < n; i++) {
        
        let arr = [];
        
        for (let j=0; j< m; j++) {
            let total = 0;
            
            for (let k=0; k< t; k++) {
                total += arr1[i][k] * arr2[k][j];
            }
            arr.push(total);
        }
        
        answer.push(arr);
    }
    
    return answer;
}