year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
elif(year%400==0 and year%4==0):
    print("Leap year")
else:
    print("Not a leap year")