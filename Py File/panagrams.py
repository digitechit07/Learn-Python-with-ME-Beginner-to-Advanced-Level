#checks whether the given string contains all the 26 alphabets or not 
#input: ThE quick brown fox jumps over the lazy dog
#output:YES
#input:	The quick brown fox jumps over the dog
#output: NO

import string
n=input()
n=n.lower()
n=n.replace(" ","")

if set(n)>=set(string.ascii_lowercase):
  print("YES",end="")
else:
  print("NO",end="")
