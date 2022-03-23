X = int(input())
Y = [0, 1]

for i in range(2, 61):
    Y.append(Y[i - 1] + Y[i - 2])

for i in range(X):
    n = int(input())
    print("Fib({}) = {}".format(n, Y[n]))