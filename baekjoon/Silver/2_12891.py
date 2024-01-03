import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
w = input()
a, c, g, t = map(int, input().split())

d = {"A": a, "C": c, "G": g, "T": t}

tmp = {"A": 0, "C": 0, "G": 0, "T": 0}

s, e = 0, 0

print(d == tmp)

ans = 0
while e < n - 1 and s <= e:
    print(tmp)
    if d == tmp and e - s == m:
        ans += 1
        tmp[w[e]] -= 1
        e += 1
        continue

    if tmp[w[e]] > d[w[e]]:
        tmp[w[s]] -= 1
        s += 1

    else:
        e += 1
        tmp[w[e]] += 1


print(ans)
