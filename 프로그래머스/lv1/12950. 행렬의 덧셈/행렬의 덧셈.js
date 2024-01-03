function solution(arr1, arr2) {
    var answer = [];
    
    for(let i=0; i < arr1.length; i++) {
        answer.push(arr1[i].map((x, y) => arr1[i][y] + arr2[i][y]))
    }
    
    return answer;
}