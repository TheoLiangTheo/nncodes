n = int(input())
for x in range(n):
    ans = False
    d = input().split(' ')
    for i in range(len(d)):
        o = d[i]
        for j in range(i + 1,len(d)):
            ans = True
            break
    print(ans)