n , m = [int(a) for a in input().split()]
a = set([int(input()) for j in range(n)])
b = set([int(input()) for j in range(m)])

set1 = a & b
set2 = a - b
set3 = b - a

print(len(set1))
print(*sorted(set1, key=int))
print(len(set2))
print(*sorted(set2, key=int))
print(len(set3))
print(*sorted(set3, key=int))
