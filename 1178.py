X = float(input())
N = []
for i in range(100):
    if(i == 0):
        N.append(X)
    else:
        N.append(N[i - 1]/2)
    print("N[{}] = {:.4f}".format(i,N[i]))
    