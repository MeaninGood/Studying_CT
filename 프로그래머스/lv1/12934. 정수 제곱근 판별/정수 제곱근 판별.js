function solution(n) {
    const tmp = n ** 0.5;
    
    if (Number.isInteger(tmp)) return (tmp + 1) ** 2;
    else return -1;
}