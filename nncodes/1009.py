d = input().split(' ')
n = int(d[0])
threshold = int(d[1])
dan = []
numb = 0
while True:
    if len(dan) == n:
        break
    d = input().split(' ')
    for x in range(len(d)):
        a = int(d[x])
        dan.append(a)
        if a > threshold:
            numb = numb+1
print(numb)