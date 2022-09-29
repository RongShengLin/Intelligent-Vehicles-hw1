import math
n = int(input())
tau = float(input())
l = []
for i in range(n):
    P , C, T = input().split()
    l.append([int(P), float(C), float(T)])
OUT = []
for i in range(n):
    B = 0
    for j in range(n):
        if l[i][0] <= l[j][0] and l[j][1] > B:
            B = l[j][1]
    Q = B
    findsol = False
    while True:
        RHS = B
        for j in range(n):
            if l[i][0] > l[j][0]:
                RHS += (math.ceil((Q + tau) / l[j][2]) * l[j][1])
        if RHS + l[i][1] >= l[i][2]:
            findsol = False
            break
        elif Q == RHS:
            findsol = True
            break
        else:
            Q = RHS
    if findsol:
        OUT.append(Q + l[i][1])
    else:
        OUT.append(0)
        break
    print(format(OUT[i], '.4f'))