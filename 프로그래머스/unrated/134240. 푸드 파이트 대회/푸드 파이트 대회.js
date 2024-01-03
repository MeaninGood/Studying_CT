function solution(food) {
    var answer = '';
    
    let arr = [];
    for(let i=1; i < food.length; i++) {
        answer += (i.toString()).repeat(food[i] / 2);
    }
    
    answer += '0' + answer.split('').reverse().join('');
    return answer;
}