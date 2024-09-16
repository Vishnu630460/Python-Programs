n=int(input())
sum=0
for i in range(n):
    rem=n%10
    sum+=rem
    n=n//10
print(sum)