def recur(cur, hp, life):
    if hp <= 0:
        return -100000
    
    if cur == n:
        return life
    
    ret = max(recur(cur + 1, hp - arr[0][cur], life + arr[1][cur]), recur(cur + 1, hp, life))
    return ret

n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

print(recur(0, 100, 0))
