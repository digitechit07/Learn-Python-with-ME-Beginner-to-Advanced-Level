''''
1111
2222
3333
4444

n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,5):
        print(i,end="")
    print()


1234
1234
1234
1234

n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,5):
        print(j,end="")
    print()


4321
4321
4321
4321

n=int(input(":"))
for i in range(1,n+1):
    x = n
    for j in range(1,5):
        print(x,end="")
        x=x-1
    print()
    

1
2 1
3 2 1
4 3 2 1

n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
        i=i-1
    print()


5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 

n=int(input(":"))
x=0
for i in range(1,n+1):
    y=1
    for j in range(1,i+1):
        z=n-x
        print(z+y-1,end=" ")
        y+=1
    print()
    x+=1
'''
