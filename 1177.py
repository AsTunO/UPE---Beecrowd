T = int(input())
N = []
if T >= 2 and T <= 50:
    i = 0
    while (i < 1000):
        for h in range (T):
            if(i > 999):
                break
            N.append(h)
            i += 1
for i in range(1000):
    print("N[{}] = {}".format(i,N[i]))