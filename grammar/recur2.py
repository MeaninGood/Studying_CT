재귀 함수

구현                재귀 함수
완전 탐색


3자리 7진수

00
01
02
10
11
12
20
21
22

m = int(input())
for i in range(m):
    for j in range(m):
        for k in range(m):
            print(str(i) + str(j) + str(k))

m = sc.nextInt();
for(int i = 0; i < m; i++){
    for(int j = 0; j < m; j++){
        for(int k = 0; k < m; k++){
          System.out.println(i + " " + j + " " + k);
        }
    }
}

n, m을 입력 받아서 n자리 m진수를 모두 출력해라

n중 반복문 구현

3가지 템플릿
문제에 맞게 재귀 설계 X
문제를 우리가 가진 틀에 맞게 변형

2가지 템플릿 => 2차원 백트래킹

0-based

1번 => n자리 m진수 모두 출력 => 순열

n, m = map(int, input().split())

arr = [0 for i in range(n)]
def recur(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(m):
        arr[cur] = i
        recur(cur + 1)

recur(0)

오늘의 목표
n자리 m진수의 3가지 방식을 배운다. => 외운다
문제를 n자리 m진수 문제로 변형하는 법을 배운다.

3 5


3 5



2번 템플릿 => 한 케이스 내에 중복된 값이 없는 순열

n, m = map(int, input().split())
visited = [False for i in range(m)]

arr = [0 for i in range(n)]
def recur(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(m):
        if visited[i]:
            continue

        arr[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)




3번 템플릿 => 중복된 케이스를 안본다. => 조합

012

오름차순만 남긴다.
비내림차순

n, m = map(int, input().split())
arr = [0 for i in range(n)]

def recur(cur, start):
    if cur == n:
        print(*arr)
        return

    for i in range(start, m):
        arr[cur] = i
        recur(cur + 1, i + 1)

recur(0, 0)





arr = [0, 3]
visited = [True, False, False, True, False]

arr = [0, 3 5  6 ? ? ]
visited = [True, False, False, True, False, True, True, False]

public static void
recur(int cur){
if (cur == n)
{
  for (int i = 0; i < n; i++){
    System.out.print(arr[i] + " ");
  }
  System.out.println("");

  return;
}

for (int i = 0; i < m; i++){
    if (visited[i]) continue;

    arr[cur] = i;
    visited[i] = true;
    recur(cur + 1);
    visited[i] = false;
}
}






## < 2529 부등호 문제 >
# < >
# 0 2 1

# i => i, i + 1

n = int(input())
ineq = input().split()
arr = [0 for i in range(n + 1)]
visited = [False for i in range(10)]

def recur(cur):
    if cur == n + 1:
        for i in range(n):
            if ineq[i] == '<' and arr[i] > arr[i + 1]:
                return
            if ineq[i] == '>' and arr[i] < arr[i + 1]:
                return

        print(*arr)
        return

    for i in range(10)[::-1]:
        if visited[i]:
            continue

        arr[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)





## < 템플릿 1 풀어서 써보기 > ##
# n = 3, m = 5

arr = [ 0 for i in range(3)]

def recur(cur) :
    if cur == 3 :
        print(*arr)
        return
    
    for i in range(5) :
        arr[cur] = i
        recur(cur + 1)
        
recur(0)



for i in range(5) :
    arr[0] = 0
    # recur(0 + 1)
    for j in range(5) :
        arr[0] = j
        # recur(1 + 1)
        for k in range(5) :
            arr[0] = k

0 0 0
0 0 1
0 0 2
0 0 3
0 0 4
0 1 0
0 1 1


## < 템플릿 2 풀어서 써보기 > ##

# n = 3, m = 5일 때

arr = [ 0 for i in range(3)]

visited = [False for i in range(5)] # F F F F F
arr = [ 0 for i in range(3)] # 0 0 0

def recur(cur) :
    if cur == 3 :
        print(*arr)
        
    for i in range(5) : # i가 1이라고 생각해보자
        if visited[i] == True :
            continue        
        arr[cur] = i
        visited[i] = True
        # recur(0 + 1)
        
        for j in range(5) :
            if visited[j] == True :
                continue
            arr[cur] = j
            visited[j] = True
            # recur(1 + 1)
            
            for k in range(5) :
                if visited[k] == True :
                    continue
                arr[cur] = k
                visited[k] = True
                # recur(2+1) - 안 돌아가는데 그냥 적어만 둠
                
                visited[k] = False
            visited[j] = False    
        visited[i] = False
    
            
arr = [0, 0, 0]

visited[i] = [True, False, False, False, False] # 0일 때
visited[j] = [False, True, False, False, False] # 1일 때
visited[k] = [True, False, False, False, False] # 0일 때 - continue
visited[k] = [False, True, False, False, False] # 1일 때 - continue
visited[k] = [False, False, True, False, False] # 2일 때 - arr[2] = 2
visited[k] = [False, False, False, True, False] # 3일 때 - arr[2] = 3
visited[k] = [False, False, False, False, True] # 4일 때 - arr[2] = 4

0 0 0 # 얘 안 함, 이미 visited[i]에서부터 True임
0 0 1 # 얘 안 함
0 0 2 # 얘 안 함
0 0 3 # 얘 안 함
0 0 4 # 얘 안 함
0 1 0 # 얘 안 함
0 1 1 # 얘 안 함
0 1 2 # 얘 함
0 1 3 # 얘 함
0 1 4 # 얘 함
0 2 0 # 얘 안 함



## < 템플릿 3 풀어서 써보기 > ##

# 비내림차순만 남기기
# n = 3, m = 5
'''
# 012 - 얘만 출력
# 021 - 밑으로는 실질적으로 같으니까 안 봄
# 102
# 120
# 201
# 210
# ...

'''

n, m = map(int, input().split())
arr = [0 for i in range(m)]

def recur(cur, start) :
    if cur == n :
        print(*arr)
        return
    
    for i in range(start, m) :
        arr[cur] = i
        recur(cur + 1, i + 1)
        
recur(0, 0)

# n = 3, m = 5 일 때

def recur(cur, start) :
    if cur == n :
        print(*cur)
        
    for i in range(0, 5) : # start : 0 -> 1 -> 2
        arr[cur] = i # arr[0]
        # recur(0 + 1, i + 1)
        for j in range(1, 5) : # start : 1 -> 2 -> 3
            arr[cur] = j #arr[1]
            # recur(1 + 1, i + 1)
            for k in range(2, 5) : # start : 2 -> 3 -> 4
                arr[cur] = k # arr[2]

recur(0, 0)

# for문 돌 때마다 start값이 1씩 증가하며 수열 생성
        
0 1 2
0 1 3
0 1 4
0 2 3
0 2 4
0 3 4
1 2 3
1 2 4
1 3 4
2 3 4
