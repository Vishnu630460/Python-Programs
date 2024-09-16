n=int(input())
n1=[]
for i in range(1,n+1):
    if n%i==0:
        n1.append(i)
for i in n1:
    print(i,end=" ")
