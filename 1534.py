while True:
    try:
        n = int(input())

        m=[]

        for i in range(n):
            m.append([])
            for j in range(n):
                m[i].append('3')

            c1 = n - 1
          
        for i in range(n):
            m[i][i] = '1'
            m[i][c1] = '2'
            c1 -= 1
            M = ''.join(m[i])
            print(M)
    except EOFError:
        break
