def num(q):
    if input() == 'YES':
        a.intersection_update(q)
    else:
        a.difference_update(q)
    return a    
        
n = int(input())
a = set(i for i in range(1, n + 1))
o = input()
while o != 'HELP':
    a = num(set(i for i in o.split()))
    o = input()
print(' '.join(str(i) for i in a))
