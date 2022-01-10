# 1268번_임시 반장 정하기

## 1~5학년까지 한 번이라도 같은 반이었던 사람이 가장 많은 학생 임시 반장
## 첫째 줄에 반의 학생 수를 나타내는 정수
## 둘째 줄부터 1번 학생부터 차례대로 각 줄마다 1~5학년까지
## 몇 반에 속했었는지 나타내는 5개의 정수 주어짐
## 첫 줄에 임시 반장으로 정해진 학생 번호 출력
## 단, 임시 반장 될 수 있는 학생 여러 명인 경우 가장 작은 번호 출력


N = int(input())

students = [list(map(int, input().split())) for _ in range(N)]

mx = -1
idx = 0

for i in range(N) :
    cnt = 0
    for j in range(1, N) :
        for k in range(5) :
            if students[i][k] == students[j][k] :
                cnt += 1
    if (mx < cnt) :
        mx = cnt
        idx = i
print(idx)