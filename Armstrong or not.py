n=int(input())
sum=0
d=str(n)
no_of_digits=len(d)
count=0
temp=n
while n>0:
    r=n%10
    sum+=r**no_of_digits
    n=n//10
    count+=1
if sum==temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")