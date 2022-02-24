# 백트래킹
# 1~4번 템플릿 => 문제를 볼 때 어디까지 템플릿을 이용핳 수 있는지
# 문제별로 어떤 부분을 구현해야 하는지

n = int(input())
# arr = [0 for i in range(100)]

def check(cur, s):
    for i in range(1, cur // 2 + 1):
        if s[-i : 0] == s[-2 * i : -i]:
            return False
        
    return True

def recur(cur, s):
    if not check(cur, s):
        return
    
    if cur == n :
        print(s)
        exit()
        return
    
    for i in range(1, 4):
        s[cur] = i
        recur(cur + 1, s + str(i))