n = int(input())
s = set(range(1,n+1))
x = s
while True:
    s1 = input()
    if s1 == 'HELP':
        print(*sorted(x))
        break
    s1 = {int(i) for i in s1.split()}
    if len(x & s1) > len(x)/2:
        print('YES')
        x &= s1
    else:
        print('NO')
        x &= s - s1
