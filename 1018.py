x = int(input())
print(x)

y100 = x // 100
x = x - y100*100
y50 = x // 50
x = x - y50*50
y20 = x // 20
x = x - y20*20
y10 = x // 10
x = x - y10*10
y5 = x // 5
x = x - y5*5
y2 = x // 2
x = x - y2*2
y1 = x // 1
x = x - y1*1

print('{} nota(s) de R$ 100,00'.format(y100))
print('{} nota(s) de R$ 50,00'.format(y50))
print('{} nota(s) de R$ 20,00'.format(y20))
print('{} nota(s) de R$ 10,00'.format(y10))
print('{} nota(s) de R$ 5,00'.format(y5))
print('{} nota(s) de R$ 2,00'.format(y2))
print('{} nota(s) de R$ 1,00'.format(y1))
