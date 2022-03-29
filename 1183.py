op = input()
M = []

for i in range(12):
    M.append([])
    for j in range(12):
        x = float(input())
        M[i].append(x)

if (op == 'S'):
    sumtot = 0
    aux = 1
    for i in range(0,11):
        for j in range(c,12):
            sumtot += M[i][j]
        aux += 1
    print('{:.1f}'.format(aux))

if (op == 'M'):
    sumtot = 0
    aux = 1
    aux2 = 0
    for i in range(0,11):
        for j in range(c,12):
            sumtot += M[i][j]
            aux2 += 1
        aux += 1
    print('{:.1f}'.format(sumtot/aux2))
