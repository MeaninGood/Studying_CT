function solution(n) {
    var answer = [];
    
    const tmp = n.toString();
    
    for(let i = tmp.length - 1; i >= 0; i--) {
        answer.push(Number(tmp[i]));
    }

    return answer;
}