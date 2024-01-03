function solution(sizes) {
    var answer = 0;
    
    let x = [];
    let y = [];
    
    for(size of sizes) {
        x.push(Math.max(size[0], size[1]));
        y.push(Math.min(size[0], size[1]));
    }
    
    answer = Math.max.apply(null, x) * Math.max.apply(null, y);
    
    return answer;
}