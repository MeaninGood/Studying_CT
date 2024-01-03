function solution(n)
{
    var answer = 0;
    const tmp = n.toString();
    
    for (let i = 0; i < tmp.length; i++) {
        answer += Number(tmp[i]);
    }
    

    return answer;
}