n=int(input())
n1=0
n2=1
print(n1,n2,end=',')
for i in range(1,n+1):
    nextele=n1+n2
    n1=n2
    n2=nextele
    print(nextele,end=',')