while True:

    n = int(input())
    if n == 0: break

    m = [[0]*n]*n

    for i in range(n):
        for j in range(n):
            
            if(i < n - i - 1):
                dl = i
            else:
                dl = n - i - 1

            if(j < n - j - 1):
                dc = j
            else:
                dc = n - j - 1
            
            if(dc < dl):
                d = dc
            else:
                d = dl
            
            print(d+1, end=' ')
        print("")
