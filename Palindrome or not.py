n=int(input())
sum=0
temp=n
while n>0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if sum==temp:
    print('Palindrome')
elif(sum!=temp):
    print("Not")
