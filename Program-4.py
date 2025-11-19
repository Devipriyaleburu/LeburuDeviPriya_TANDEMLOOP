"""using python program4"""
li=list(map(int,input().split()))
d= {}
for i in range(1, 10):
    c= 0
    for n in li:
        if n % i == 0:
            c += 1
    d[i] = c
print(d)


