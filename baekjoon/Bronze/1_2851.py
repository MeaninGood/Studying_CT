'''
n = [int(input()) for _ in range(10)]

score = 0

for i in n :
    score += i

    if score >= 100 :

        if abs(score-100) <= abs(score-100-i) : 
            print(score)
            break

        elif abs(score-100) > abs(score-100-i) :
            print(score-i)
            break
        
if score < 100 :
    print(score)
'''


arr = [int(input()) for _ in range(10)]

ans = 0
for i in range(10):
    ans += arr[i]
    
    if ans >= 100 and abs(ans - 100) > abs(ans - 100 - arr[i]):
        ans -= arr[i]
        break
        
        
print(ans)