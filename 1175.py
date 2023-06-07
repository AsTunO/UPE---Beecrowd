N = []
for i in range (20):
    N.append(int(input()))
X = list(reversed(N))
for i in range(20):
    print("N[{}] = {}".format(i, X[i]))
    
