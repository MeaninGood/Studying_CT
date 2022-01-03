# 10871번_X보다 작은 수

## 정수 N개로 이루어진 수열 A와 정수 X가 주어짐
## A에서 X보다 작은 수를 모두 출력하는 프로그램 작성
## 첫째 줄에 N과 X 주어짐, 둘째 줄에 수열 A를 이루는 정수 N개 주어짐


N, X = map(int, input().split())
A = list(map(int, input().split()))

B = [A[i] for i in range(N) if A[i] < X]

print(*B)
#그냥 print(B)로 쓰면 : [1, 2, 3] 의 형태로 출력됨
#print(*B)로 쓰면 : 1 2 3 으로 출력됨 -> 대괄호와 쉼표 삭제, 공백만 남음



