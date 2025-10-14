#deletes consecutive vowels in the string and returns the string in the same order
#input:great part of life is eating eel
#output:gret part of life is eting el

n=input()
n=n.lower()
n=n+" "     #to prevent the index out of bound error in the while loop below
for i in range(len(n)):
    if n[i] in 'aeiou':
        while True and i!=(len(n)-2):
            if n[i+1] in 'aeiou':
                n=n[:i+1]+"$"+n[i+2:]
                i+=1
            else:
                break
    else:
        continue
                
n=n.strip()
print(n.replace("$",""),end="")
