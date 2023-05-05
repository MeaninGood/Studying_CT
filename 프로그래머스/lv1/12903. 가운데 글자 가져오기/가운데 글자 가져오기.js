function solution(s) {
    var answer = '';
    
    if (s.length % 2) answer += s[Math.floor(s.length / 2)];
    else {
        answer += s[s.length / 2 - 1];
        answer += s[s.length / 2];
    }
    
    return answer;
}