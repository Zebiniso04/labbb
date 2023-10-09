n=int(input())
a1= int(input())
s1=set()
for i in range(a1):
    s1.add(input())
a2=int(input())
s2=set()
for i in range(a2):
    s2.add(input())
a3=int(input())
s3=set()
for i in range(a3):
    s3.add(input())
k1=s1&s2&s3
k1=sorted(s1&s2&s3,key=str)
print(len(k1))
for i in k1:
    print(i)
k1=s1|s2|s3
k1=sorted(s1|s2|s3,key=str)
print(len(k1))
for i in k1:
    print(i)
