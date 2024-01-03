arr = [int(input()) for _ in range(10)]

ans = 0
for i in range(10):
    ans += arr[i]
    
    if ans >= 100 and abs(ans - 100) > abs(ans - 100 - arr[i]):
        ans -= arr[i]
        break
        
        
print(ans)