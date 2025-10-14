'''1. Two sum'''

input = [1, 2, 3, 4]
target = 4
output = []
flag = 0
for i in range(len(input)-1):
    for j in range(len(input)-1,i,-1): 
        if input[i] + input[j] == target:
            output.append(i)
            output.append(j)
            flag = 1
        else:
            continue
    if flag == 1:
        break

if flag == 1:
    print(output)
else:
    print('Target value cannot be obtained')