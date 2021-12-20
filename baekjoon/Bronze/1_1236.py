# 1236번_성 지키기

## 직사각형 모양의 성 모든 행과 열에 경비원 배치, 필요한 최소 경비원 수
## 첫째 줄 세로 크기 N과 가로 크기 M, N개의 줄에 성의 상태 주어짐
## 성의 상태 .은 빈칸, X는 경비원이 있는 칸
## 2 4
## .X..
## ...X

N, M = map(int, input().split())

castle = [] #리스트 미리 만들어 두기
for x in range(N) : #N의 개수만큼 입력창 생성
    castle.append(input()) #미리 만들어둔 리스트에 변수 추가. ex) [[X,X,X,X],[X,.,.,X]]

a = 0 #가로 탐색. 즉 castle[i][j]에서 [i] 탐색
b = 0 #세로 탐색. 즉 castle[i][j]에서 j 고정해두고 [i] 탐색

for i in range(N) :
    if 'X' not in castle[i] : #castle[i]에 'X'가 없다면
        a += 1 #가로 탐색에 0추가.

for j in range(M) :
    if 'X' not in [castle[i][j] for i in range(N)] : #j 고정해두고 i돌린 리스트에서 찾기
        b += 1 #세로 탐색에 추가.

print(max(a,b)) #둘 중 큰 값이 최소 필요 경비원 수