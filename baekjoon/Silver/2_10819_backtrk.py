# 10819번_차이를 최대로

## N개의 정수로 이루어진 배열 A
## 배열의 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성
## |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

'''
# 첫째 줄에 N (3 ≤ N ≤ 8)
# 둘째 줄에는 배열 A에 들어있는 정수
# 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
## 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력

(입력)
6
20 1 15 8 4 10

(출력)
62

'''

n = int(input())
arr = list(map(int, input().split()))
arr2 = [ 0 for i in range(n)]
visited = [ False for i in range(n)]


def recur(cur):
    if cur == n:
        total = 0
        for i in range(1, n):
            total += abs(arr[arr2[i]] - arr[arr2[i-1]])
            
        return total
    
    total = 0 
    for i in range(n):
        if visited[i]:
            continue
        
        arr2[cur] = i
        visited[i] = True
        total = max(total, recur( cur + 1 ))
        visited[i] = False
        
    return total


print(recur(0))