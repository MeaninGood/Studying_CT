function solution(arr) {
    var answer = 0;
    
    const tmp = arr.reduce((sum, cur) => sum + cur);
    answer = tmp / arr.length;
    
    return answer;
}