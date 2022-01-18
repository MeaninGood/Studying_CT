# 2751번_수 정렬하기 2

## N개의 수가 주어졌을 때, 이를 오름차순으로 정렬

'''
# 첫째 줄에 수의 개수 N, 둘째 줄부터 N개의 줄에는 수가 주어짐, 중복 없음
## 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력

(입력 - \n 기준) 5 5 4 3 2 1 
(출력 - \n 기준) 1 2 3 4 5

'''


'''
#### 이거 python3로 돌리면 시간 초과 뜸 (귀한 것) ####
#### pypy로 돌리면 메모리 223584kB, 1420ms 
n = int(input())

li = []
for i in range(n) :
    li.append(int(input()))
    
for i in sorted(li) :
    print(i)
'''




# 83508KB, 1472ms
import sys
n = int(sys.stdin.readline())

li = []
for i in range(n) :
    li.append(int(sys.stdin.readline().strip()))
    
for i in sorted(li) :
    print(i)



# 위랑 아래 속도 똑같은지 비교해보기



'''똑같음!!!
from sys import stdin
n = int(stdin.readline())

li = []
for i in range(n) :
    li.append(int(stdin.readline().strip()))
    
for i in sorted(li) :
    print(i)

'''


