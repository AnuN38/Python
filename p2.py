p = [100,80,60,70,60,75,85]
n = len(p)
s = [None] * n
s[0] = 1
for i in range(1,n):
    s[i] = 1
    j = i-1
    while j >=0 and p[i] > p[j]:
        s[i] += 1
        j = j - 1
for i in range(n):
    print(s[i],end=" ")
