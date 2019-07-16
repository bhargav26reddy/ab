n=int(input())
l=list(map(int,input().split()))
l.sort()
b=l[::-1]
l=len(b)
c=0
for i in range(l):
    if(b[i]==0):
        c+=1
if(c==l):
    print("0")
else:
    for i in b:
        print(i,end="")
