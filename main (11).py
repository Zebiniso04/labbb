a=set(input().split())
b=set(input().split())
counts=len(a)+len(b)
a.update(b)
print(counts-len(a))
