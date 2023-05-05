function solution(numbers) {
    
    // const tmp = numbers.reduce(function add(sum, currentValue) {
    //     return sum + currentValue;
    // });
    
    const tmp = numbers.reduce((sum, currentValue) => sum + currentValue);
    
    return tmp / numbers.length;
}