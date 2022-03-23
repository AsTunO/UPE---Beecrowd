x = int(input())

years = x // 365
x = x - years * 365
months = x // 30
x = x - months * 30
days = x

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))