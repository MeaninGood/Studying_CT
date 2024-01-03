function solution(s) {
    
    for(let i = 0; i < s.length; i++) {
        if(!parseInt(s[i]) && s[i] !== "0") return false;
    }
    
    if (s.length === 4 | s.length === 6) return true;
    
    return false;
}