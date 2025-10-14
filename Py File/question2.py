'''
write a python program to iterate over an enumaration class and display individual members and  
their values
'''

from enum import Enum


class Sibling(Enum):
    Amby = 30
    Simbi = 40
    Bramy = 43


for sib in Sibling:
    print('{} = {}'.format(sib.name, sib.value))
