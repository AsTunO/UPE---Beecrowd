column = int(input())
aux = input()
x = 0
M = []

sumtot = 0

for i in range(12):
    P = []
    for j in range(12):
        aux = float(input())
        P.append(aux)
    M.append(P)
    sumtot += M[i][column]


med = sumtot/3

if(aux == 'S'):
    print(sumtot)
elif(aux == 'M'):
    print(med)
