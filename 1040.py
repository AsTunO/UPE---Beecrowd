n1, n2, n3, n4 = map(float, input().split())

med = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print('Media: {:.1f}'.format(med))

if (med >= 7.0):
    print('Aluno aprovado.')

if (med < 5.0):
    print('Aluno reprovado.')
    
if (5.0 <= med <= 6.9):
    print('Aluno em exame.')
    x = float(input())
    print('Nota do exame: {}'.format(x))
    med2 = (x + med) / 2
    if med2 >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(med2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(med2))