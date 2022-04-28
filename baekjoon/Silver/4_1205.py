import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())

if n == 0:
    print(1)

else:
    arr = list(map(int, input().split()))

    arr.append(m)
    arr.sort(reverse=True)
    print(arr)
    if m == arr[-1] and len(arr) > p:
        print(-1)
        
    else:
        idx = 1
        for i in range(n + 1):
            if m == arr[i]:
                print(idx)
                break
            
            idx += 1