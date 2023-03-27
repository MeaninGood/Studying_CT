import sys

n = int(sys.stdin.readline()) 
li = []

for i in range(n) :
    li.append(sys.stdin.readline().strip())

liset = set(li)
lst = list(liset)
lst.sort()
lst.sort(key=len)


for i in lst :
    print(i, end = ' ')