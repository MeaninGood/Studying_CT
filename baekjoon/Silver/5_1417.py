# 1417번_국회의원 선거

## 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면
## 2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하여
## 기호 1번이 당선되게 하기
## 다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성

'''
# 첫째 줄에 후보의 수 N
# 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수
# 이렇게 총 N개의 줄에 걸쳐 입력이 들어옴
# N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수
## 첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력

(입력)
5 4
3 1
3 2
4 3
5 3

(출력) 
1 2

'''

m = int(input())
n = int(input())
arr = [int(input()) for _ in range(m - 1)]

cnt = 0
while arr:
    tmp = max(arr)
    
    if n > tmp:
        print(cnt)
        break

    arr.sort(reverse=True)
    arr[0] -= 1
    n += 1
    cnt += 1

else:
    print(cnt)

# while 1:
    
#     tmp = arr[0]
    
#     if n > tmp:
#         break

#     arr.sort(reverse=True)
#     print(arr)
#     arr[0] -= 1
#     n += 1
#     cnt += 1
    
# print(cnt)