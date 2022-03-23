x = int(input())
hrs = x // 60**2
x = x - hrs * 60**2

mins = x // 60
x = x - mins*60

sec = x

print('{}:{}:{}'.format(hrs, mins, sec))