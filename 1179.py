P = [0] * 5
I = [0] * 5

index1 = 0
index2 = 0

for i in range(15):
    aux = int(input())
    if(aux % 2 == 0):
        if(index1 < 5):
            P[index1] = aux
            index1 += 1
        else:
            for j in range(5):
                print("par[{}] = {}".format(j, P[j]))
            index1 = 0
            P[index1] = aux
            index1 += 1

    else:
        if(index2 < 5):
            I[index2] = aux
            index2 += 1
        else:
            for j in range(5):
                print("impar[{}] = {}".format(j, I[j]))
            index2 = 0
            I[index2] = aux
            index2 += 1

for i in range(index2):
    print("impar[{}] = {}".format(i, I[i]))
for i in range(index1):
    print("par[{}] = {}".format(i, P[i]))
