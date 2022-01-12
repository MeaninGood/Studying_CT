# 4435번_중간계 전쟁

## 간달프점수 : 호빗1, 인간2, 엘프3, 드워프3, 독수리4, 마법사10
## 사우론점수 : 오크1, 인간2, 워그2, 고블린2, 우럭하이3, 트롤5, 법사10
## 전투에 참여한 각 종족의 점수 합한 뒤, 어느 쪽이 이기나
## 첫째 줄 전투 개수 T, 각 전투는 두 줄로 이루어짐
## 첫째 줄에 간달프팀 종족 수, 순서 위와 동일
## 둘째 줄 사우론팀 종족 수, 순서 위와 동일
## 각 전투에 대해 "Battle"과 전투 번호 출력
## 간달프 승 : "Good triumphs over Evil"
## 사우론 승 : "Evil eradicates all trace of Good"
## 무승부 : "No victor on this battle field" 출력


import sys

t = int(input()) # 전투 개수 t
gan = [1, 2, 3, 3, 4, 10] # 간달프팀의 각 종족별 점수
sau = [1, 2, 2, 2, 3, 5, 10] # 사우론팀의 각 종족별 점수

battle = 0
for i in range(t) : # 전투 개수만큼 간달프팀과 사우론팀의 참여자 수가 주어짐
    gnum = list(map(int, sys.stdin.readline().split())) #간달프팀 종족별 참여자 수
    snum = list(map(int, sys.stdin.readline().split())) #사우론팀 종족별 참여자 수

    gscore = 0
    sscore = 0

    for j in range(len(gnum)) :
        gscore += gan[j] * gnum[j] #간달프 종족별 점수 * 종족별 참여자 수
    
    for k in range(len(snum)) :
        sscore += sau[k] * snum[k] #사우론 종족별 점수 * 종족별 참여자 수

    battle += 1 # 전투 번호

    if gscore > sscore : #간달프팀 승리 시
        print(f'Battle {battle}: Good triumphs over Evil')

    elif gscore < sscore : #사우론팀 승리시
        print(f'Battle {battle}: Evil eradicates all trace of Good')

    else : #무승부
        print(f'Battle {battle}: No victor on this battle field')


    