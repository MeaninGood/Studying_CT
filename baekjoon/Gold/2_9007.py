'''
300 4
40 52 60 80
63 68 75 88
48 48 54 93
49 56 73 75


[103, 108, 115, 115, 120, 123, 127, 128, 128, 135, 140, 143, 148, 148, 155, 168]
[97, 97, 103, 104, 104, 110, 121, 121, 123, 123, 127, 129, 142, 149, 166, 168]



150
1 1000
1 200
100 101
99 100
'''

import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(4)]

    sum_arr1, sum_arr2 = [], []
    for sep in range(2):
        for i in range(n):
            for j in range(n):
                if sep == 0:
                    sum_arr1.append(arr[0][i] + arr[1][j])

                else:
                    sum_arr2.append(arr[2][i] + arr[3][j])

    sum_arr1.sort()
    sum_arr2.sort()

    length = n ** 2
    s, e = 0, length - 1
    x, y = sum_arr1[s], sum_arr2[e]
    while s < length and 0 <= e:
        if abs(k - (x + y)) > abs(k - (sum_arr1[s] + sum_arr2[e])):
            x, y = sum_arr1[s], sum_arr2[e]
        
        elif abs(k - (x + y)) == abs(k - (sum_arr1[s] + sum_arr2[e])) and x + y > sum_arr1[s] + sum_arr2[e]:
                x, y = sum_arr1[s], sum_arr2[e]

        if sum_arr1[s] + sum_arr2[e] < k:
            s += 1
            
        else:
            e -= 1

    print(x + y)