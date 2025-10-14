'''
1
12
123
1234

n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


1
23
345
4567

n=int(input(":"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
        i+=1
    print()
    

1
23
456
78910

n=int(input(":"))
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(x,end="")
        x=x+1
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


1
1 1
2 0 2
3 0 0 3

n=int(input(":"))
print("1")
for i in range(1,n):
    j=0
    for j in range(0,i+1):
        if j==0 or j==i:
            print(i,end=" ")
        else:
            print("0",end=" ")
        j+=1
    print()
    i+=1
'''
