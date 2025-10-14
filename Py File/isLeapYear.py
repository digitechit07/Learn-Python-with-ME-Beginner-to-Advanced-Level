#Given a year find if it a leap year or not

year = int(input())

if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")

elif (year % 4 ==0) and (year % 100 != 0):
    print("Leap year")

else:
    print("not a leap year")

N=int(input())
i=1
while(i<=N):
    print(i, end = '')
    i=i+1

N=int(input())
count=0
while(N>0):
    N=N//10
    count=count+1
print(count)


N=int(input())

while(N>0):
    d=N%10
    print(d,end="")
    N=N//10