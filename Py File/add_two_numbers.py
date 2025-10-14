'''Leetcode problem list Q2'''

'''Add two numbers'''

l1 = []
n1 = int(input('Enter the number of elements in the first list: '))
for i in range(n1):
    num = int(input('Enter the element to be added in the list: '))
    l1.append(num)

l2 = []
n2 = int(input('Enter the number of elements in the second list: '))
for i in range(n2):
    num = int(input('Enter the element to be added in the list: '))
    l2.append(num)

num1 = int(''.join(map(str,l1)))
num2 = int(''.join(map(str,l2)))

def reverse(a):
    rev_num = 0
    while a > 0:
        digit = a % 10
        rev_num = rev_num * 10 + digit
        a //= 10
    return rev_num

rev_num1 = reverse(num1)
rev_num2 = reverse(num2)

output_list = []
output = rev_num1 + rev_num2
temp = output
if temp == 0:
    output_list.append(temp)
else:
    while temp > 0:
        digit = temp % 10
        output_list.append(digit)
        temp //= 10

# print(output)
print(output_list)



# print(rev_num1,rev_num2)
# print(num1)
# print(num2)
# print(l1,l2)