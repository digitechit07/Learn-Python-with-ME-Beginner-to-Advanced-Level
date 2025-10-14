"""Given two dictionaries, write a program for creating a dictionary 
in such a way that it consists of all the keys that are common in both dictionaries. 
The values corresponding to the keys in this new dictionary 
are the sum of the values of those keys in the two dictionaries."""
#Sample Input
"""
a b c
1 2 3
c d e
4 5 6
"""
#Sample Output
#{'c': 7}

def commonKey(dict1, dict2):
    dict3 = {}
    for k1,v1 in dict1.items():
        for k2,v2 in dict2.items():
            if(k1==k2):
                sum=v1+v2
                k3=k1
                dict3[k3]=sum
                print(dict3)
    else:
        print(dict3)