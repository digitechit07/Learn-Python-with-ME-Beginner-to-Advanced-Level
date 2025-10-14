'''
write a python to create an ENUM object and  display member name and value

sample data:
 Amby= 48
 Simbi= 32
 Bramy = 33

 Exprected output 
 Member name: Amby
 Member value: 48
'''

from enum import Enum


class Sibling(Enum):
    Amby = 23
    Simbi = 34
    Bramy = 32


print('\nMember name: {}'.format(Sibling.Amby.name))
print('Member value: {}'.format(Sibling.Amby.value))
