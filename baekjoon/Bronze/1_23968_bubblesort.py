# 23968번_알고리즘 수업 - 버블 정렬 1

## 버블 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수


'''
# 첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 10,000)
# 교환 횟수 K(1 ≤ K ≤ N2)가 주어짐
# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진
## K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력
## 교환 횟수가 K 보다 작으면 -1을 출력

(입력)
6 10
4 6 5 1 3 2

(출력)
2 4

'''

n, k = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            cnt += 1
            
            if cnt == k:
                print(arr[j], arr[j+1])
                break
            
if cnt < k:
    print(-1)
            
