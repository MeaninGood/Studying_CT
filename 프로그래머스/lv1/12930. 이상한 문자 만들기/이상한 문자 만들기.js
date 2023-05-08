function solution(s) {
    let arr = s.split(" ");
    
    var answer = '';
    for(i of arr) {
        for(let j=0; j<i.length;j++) {
            if(j%2 === 0) answer += i[j].toUpperCase();
            else answer += i[j].toLowerCase();
        }
        answer += ' '
    }
    
    return answer.substr(0, answer.length - 1);
}