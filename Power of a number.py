n=int(input())
p=int(input())
#print(pow(n,p))
out=1
for i in range(p):
    out*=n
print(out)