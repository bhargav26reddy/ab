n=int(input())
v=list(map(int,input().split()))
z=[]
for i in v:
    b=v.count(i)
    if b>=2 and i not in z:
        z.append(i)
if(len(z)==0):
    print("unique")
for i in z:
    print(i,end=" ")
