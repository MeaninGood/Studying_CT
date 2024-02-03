import sys

input = lambda: sys.stdin.readline().strip()

A, B, C = map(int, input().split())

arrA = sorted(map(int, input().split()))
arrB = sorted(map(int, input().split()))
arrC = sorted(map(int, input().split()))


def check(target, arr):
    s, e = 0, len(arr) - 1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            return target
        if arr[mid] < target:
            s = mid + 1
        elif arr[mid] > target:
            e = mid - 1


ans = 1 << 31
for anum in arrA:
    for bnum in arrB:
        target = (anum + bnum) // 2
        tmp1 = check(target, arrC)
        score1 = max(anum, bnum, tmp1) - min(anum, bnum, tmp1)

        tmp2 = check(target, arrA)
        score2 = max(bnum, anum, tmp2) - min(bnum, anum, tmp2)

        ans = min(ans, min(score1, score2))

print(ans)