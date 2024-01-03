function solution(strings, n) {
    strings.sort();
    strings.sort((a, b) => {
        if (a[n] > b[n]) return 1;
        if (a[n] < b[n]) return -1;
        return 0;
        
    });
    return strings;
}