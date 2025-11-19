a = int(input())
if a % 2 != 0:
    t=a
else:
    t=a - 1
l = []
for i in range(1, a+ 1, 2):
    l.append(i)
print(l)