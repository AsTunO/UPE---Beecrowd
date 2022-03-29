line = int(input())
aux = input()
x = 0
M = []

for i in range(3):
    P = []
    for j in range(3):
        aux = float(input())
        P.append(aux)
    M.append(P)

sumtot = sum(M[line])
med = sumtot/3

if(aux == 'S'):
    print(sumtot)
elif(aux == 'M'):
    print(med)

