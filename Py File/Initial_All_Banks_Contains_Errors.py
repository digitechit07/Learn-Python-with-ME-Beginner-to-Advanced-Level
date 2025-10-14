##################
#below creates private ip addresses. 
import ipaddress
import random
import operator
from socket import inet_ntoa
from struct import pack
#from scapy.all import *

#### |||||| seems to work  finding the smallest subnet that also
#### vvvvvv contains all the networks given.
ADDRESS_ANY = ipaddress.ip_address(u'0.0.0.0')
def one_net(subnets):
    """
    Get the one IP network that covers all subnets in input,
    or None is subnets are disjoint.
    """
    if len(subnets) == 0:
        return None

    minlen = min([net.prefixlen for net in subnets])
    while subnets.count(subnets[0]) < len(subnets) and minlen > 0:
        # all subnets are not (yet) equal
        subnets = [net.supernet(new_prefix=minlen) for net in subnets]
        minlen -= 1

    # 0.0.0.0/? -> no common subnet
    if subnets[0].network_address == ADDRESS_ANY:
        return None
    return subnets[0]

#print(one_net(nets))

### ||||||
### vvvvvv function to generate a random A, B, or C ip address. unless 10, 172, or 192
### |||||| is passed then firstoct is set to that and that class ip is generated.
### vvvvvv Remeber that Info is returned in a tuple and must be set to a varilbe/list 
### |||||| to be called.
### vvvvvv

def randABCnet(x=""):
    #determine class A, B, or C
    classes = [10, 172, 192]
    if x == "":
        firstoct = classes[random.randint(0, 2)]
    elif x in classes:
        firstoct = x
    else:
        print("!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!  X =/= to a A, B, or C ip")
        print("!!!!!!!!!!!!!!!!!!!")
        return
    # Actually do some work (make ip and other info)
    if firstoct == 10:
        IPaddr = str(10) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))    
        Masknum = random.randint(8, 30)
    elif firstoct == 172:
        IPaddr = str(172) + "." + str(random.randint(16, 32)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(12, 30)
    elif firstoct == 192:
        IPaddr = str(192) + "." + str(168) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(16, 30)
    Mask = '/' + str(Masknum)
    Network = ipaddress.IPv4Network(IPaddr + Mask, False)
    Broadcast = Network.broadcast_address
    bits = 0xffffffff ^ (1 << 32 - Masknum) - 1
    subnetmask = inet_ntoa(pack('>I', bits))
    return Mask, Network, Broadcast, subnetmask, IPaddr, Masknum
#            0      1         2          3         4        5

def randABClargernet(x=""):
    #determine class A, B, or C
    classes = [10, 172, 192]
    if x == "":
        firstoct = classes[random.randint(0, 2)]
    elif x in classes:
        firstoct = x
    else:
        print("!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!  X =/= to a A, B, or C ip")
        print("!!!!!!!!!!!!!!!!!!!")
        return
    # Actually do some work (make ip and other info)
    if firstoct == 10:
        IPaddr = str(10) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))    
        Masknum = random.randint(8, 24)
    elif firstoct == 172:
        IPaddr = str(172) + "." + str(random.randint(16, 32)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(12, 24)
    elif firstoct == 192:
        IPaddr = str(192) + "." + str(168) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(16, 24)
    Mask = '/' + str(Masknum)
    Network = ipaddress.IPv4Network(IPaddr + Mask, False)
    Broadcast = Network.broadcast_address
    bits = 0xffffffff ^ (1 << 32 - Masknum) - 1
    subnetmask = inet_ntoa(pack('>I', bits))
    return Mask, Network, Broadcast, subnetmask, IPaddr, Masknum
#            0      1         2          3         4        5

#Info = randABCnet(10)
#print(Info[0])
#print(Info[2])
#print(Info[3])

def randnet():
    reserved = [198, 203, 127, 224, 240, 100, 0, 169, 255]
    firstoct = random.randint(1, 254)
    while firstoct in reserved:
        firstoct = random.randint(1, 254)
    if firstoct == 10:
        IPaddr = str(10) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))    
        Masknum = random.randint(8, 30)
    elif firstoct == 172:
        IPaddr = str(172) + "." + str(random.randint(16, 32)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(12, 30)
    elif firstoct == 192:
        IPaddr = str(192) + "." + str(168) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(16, 30)
    else: 
        IPaddr = str(firstoct) + "." + str(168) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(8, 30)
    Mask = '/' + str(Masknum)
    Network = ipaddress.IPv4Network(IPaddr + Mask, False)
    Broadcast = Network.broadcast_address
    bits = 0xffffffff ^ (1 << 32 - Masknum) - 1
    subnetmask = inet_ntoa(pack('>I', bits))
    return Mask, Network, Broadcast, subnetmask, IPaddr, Masknum

#modified from the one above to create larger networks for summerzation questions.
def randlargernet():
    reserved = [198, 203, 127, 224, 240, 100, 0, 169, 255]
    firstoct = random.randint(1, 254)
    while firstoct in reserved:
        firstoct = random.randint(1, 254)
    if firstoct == 10:
        IPaddr = str(10) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))    
        Masknum = random.randint(8, 24)
    elif firstoct == 172:
        IPaddr = str(172) + "." + str(random.randint(16, 32)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(12, 24)
    elif firstoct == 192:
        IPaddr = str(192) + "." + str(168) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(16, 24)
    else: 
        IPaddr = str(firstoct) + "." + str(168) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        Masknum = random.randint(8, 24)
    Mask = '/' + str(Masknum)
    Network = ipaddress.IPv4Network(IPaddr + Mask, False)
    Broadcast = Network.broadcast_address
    bits = 0xffffffff ^ (1 << 32 - Masknum) - 1
    subnetmask = inet_ntoa(pack('>I', bits))
    return Mask, Network, Broadcast, subnetmask, IPaddr, Masknum

SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme. 
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix


"""
# Decimal to Binary conversion questions
file = open('dectobin.txt','a') 
number = 0
while  number <= 255:
    file.write("FIB" + '\t'  + "Convert the decimal number " + str(number) + " to an 8 bit binary number." + '\t' + '{0:08b}'.format(number) + "\n") 
    print('{0:08b}'.format(number))
    number += 1
file.close() 
"""

"""
# Decimal to Hex conversion questions
file = open('dectohex.txt','a') 
number = 0
while  number <= 255:
    file.write("FIB" + '\t'  + "Convert the decimal number " + str(number) + " to a hex number." + '\t' + '{0:02x}'.format(number) + '\t' + '{0:02X}'.format(number) + "\n") 
    print('{0:02X}'.format(number) + " " + '{0:02x}'.format(number))
    number += 1   
file.close() 
"""

"""
# Binary to Decimal 
file = open('bintodec.txt','a') 
number = 0
while  number <= 255:
    file.write("FIB" + '\t'  + "Convert the 8 bit binary number " + '{0:08b}'.format(number) + " to a decimal number." + '\t' + str(number) + "\n") 
    print(str(number))
    number += 1   
file.close()
"""

"""
# Binary to Decimal 
file = open('bintohex.txt','a') 
number = 0
while  number <= 255:
    file.write("FIB" + '\t'  + "Convert the 8 bit binary number " + '{0:08b}'.format(number) + " to a hex number." + '\t' + '{0:02x}'.format(number) + '\t' + '{0:02X}'.format(number) + "\n") 
    print(str(number))
    number += 1   
file.close()
"""

"""
# hex to Decimal 
file = open('hextodec.txt','a') 
number = 0
while  number <= 255:
    file.write("FIB" + '\t'  + "Convert the hex number " + '{0:02X}'.format(number) + " to a decimal number." + '\t' + str(number) + "\n") 
    print(str(number))
    number += 1   
file.close()
"""

"""
# hex to Binary 
file = open('hextobin.txt','a') 
number = 0
while  number <= 255:
    file.write("FIB" + '\t'  + "Convert the hex number " + '{0:02X}'.format(number) + " to a 8 bit binary number." + '\t' + '{0:08b}'.format(number) + "\n") 
    print(str(number))
    number += 1   
file.close()
"""

"""
# Broadcast Address for a network
import random
import ipaddress

file = open('broadcastquestions.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    file.write("FIB" + '\t'  + "What is the broadcast address for the " + str(Network) + " network" + '\t' + str(Broadcast) + "\n") 
    print(str(number))
    number += 1  
file.close()
"""

"""
# total hosts on a network question
import random
import ipaddress

file = open('totalhostsquestions.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABCnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    file.write("FIB" + '\t'  + "Including the network and broadcast addresses what is the maximum number of hosts on the " + str(Network) + " network?" + '\t' + str(Network.num_addresses) + "\n") 
    print(str(number))
    number += 1  
file.close()
"""

"""
# questions about total number of hosts on a network
import random
import ipaddress

file = open('#ofhostsquestions.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABCnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    numofhosts = random.randint(1, int(Network.num_addresses) * int(2))
    if numofhosts <= Network.num_addresses:
        file.write("TF" + '\t'  + "True or False. There are at least " + str(numofhosts) + " hosts on the " + str(Network) + " network?" + '\t' + "true" + "\n") 
    elif numofhosts >= Network.num_addresses: 
        file.write("TF" + '\t'  + "True or False. There are at least " + str(numofhosts) + " hosts on the " + str(Network) + " network?" + '\t' + "false" + "\n")
    print(str(number))
    number += 1  
file.close()
"""

"""
#longhand to short hand conversion; subnet to cdir
import random
import ipaddress
from socket import inet_ntoa
from struct import pack

file = open('cdirtomask.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 32:#99:
    IPaddr = str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
    Masknum = number #random.randint(8, 30)
    Mask = '/' + str(Masknum)
    Network = ipaddress.IPv4Network(IPaddr + Mask, False)
    Broadcast = Network.broadcast_address
    bits = 0xffffffff ^ (1 << 32 - Masknum) - 1
    subnetmask = inet_ntoa(pack('>I', bits))
    file.write("FIB" + '\t'  + "What is the shorthand corresponding to a subnet mask of " + subnetmask + "?" + '\t' + Mask + "\n") 
    print(str(number))
    number += 1  
file.close()
"""

"""
#is ip on a network/mask
import random
import ipaddress
from socket import inet_ntoa
from struct import pack

file = open('iponnetwork.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABCnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
    
    newNetwork = ipaddress.IPv4Network(IPaddr + '/' + str(Masknum + 1), False)
    
    iponnet = Network[random.randint(0, Network.num_addresses - 1)]
    print(Network, newNetwork, iponnet)
    if iponnet in newNetwork:
        file.write("TF" + '\t'  + "True or False. The " + str(iponnet) + " address is on the " + str(newNetwork) + " network." + '\t' + "True" + "\n")
    elif iponnet not in newNetwork: 
        file.write("TF" + '\t'  + "True or False. The " + str(iponnet) + " address is on the " + str(newNetwork) + " network." + '\t' + "False" + "\n")
    print(number)
    number += 1  
file.close()
"""

"""
# last valid host on network
file = open('lastvalidhost.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABCnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
  
    file.write("FIB" + '\t'  + "Enter the last valid host on the network " + str(Network[0]) + " " + str(subnetmask) + "." + '\t' + str(Network[Network.num_addresses-1]) + "\n")
    print(number)
    number += 1  
file.close()
"""

"""
# last valid host on network
file = open('subnethostbelongs.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABCnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
  
    file.write("FIB" + '\t'  + "Enter the subnet the host " + str(Network[random.randint(1, Network.num_addresses-2)]) + " " + str(subnetmask) + " Belongs to." + '\t' + str(Network[0]) + "\n")
    print(number)
    number += 1  
file.close()
"""

"""
# hosts per subnet
file = open('#hostspersubnet.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABCnet()
    IPaddr = information[4]
    Mask = information[0]
    Network = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
  
    file.write("FIB" + '\t'  + "What subnet mask would give " + str(Network.num_addresses - 2) + " Hosts per subnet?" + '\t' + str(Mask) + '\t' + str(subnetmask) + "\n")
    print(number)
    number += 1  
file.close()
"""

"""
# hosts per subnet
file = open('#sumupsubnets.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    classes = [10, 172, 192]
    whatclass = classes[random.randint(0,2)]
    information1 = randABCnet(whatclass)
    information2 = randABCnet(whatclass)
    information3 = randABCnet(whatclass)

    Network1 = information1[1]
    Network2 = information2[1]
    Network3 = information3[1]
    nets = [Network1, Network2, Network3]
    file.write("FIB" + '\t'  + "What is the smallest network that contains all of the following subnets: " + str(nets[0]) + " " + str(nets[1]) + " " + str(nets[2]) + "." + '\t' + str(one_net(nets)) + "\n")
    print(number)
    number += 1  
file.close()
"""

##############  Number is set below because I used it in the following
##############  3 generators to keep track of # of questions created.
##############  it can be removed here; but will need to be removed 
##############  from the generators as well
##############   
number = 1

"""
# vlsm questions basenet = 10.0.0.0/12 with host requirements of
# 500k, 250k, 125K, 60k, 30k, 30k. Asks students for one of the
# subnets randomly (1 - 6). Should always expect the same single answer
# because all IPs in the basenet are used.
file = open('vlsm_12.txt','a') 

BASEOCT1 = 10
BASEOCT2 = 0
BASEOCT3 = 0
BASEOCT4 = 0

OCT1 = BASEOCT1
OCT2 = BASEOCT2
OCT3 = BASEOCT3
OCT4 = BASEOCT4

basemask = '/12'
subnethostnum = ['500,000', '250,000', '125,000', '60,000', '30,000', '30,000']
while BASEOCT2 <= 240:
    OCT1 = BASEOCT1
    OCT2 = BASEOCT2
    OCT3 = BASEOCT3
    OCT4 = BASEOCT4
    subnetans = random.randint(0, 5) # to pull from list
    subnetansnum = subnetans + 1 # translate to a nth spot.
    hostans = subnethostnum[subnetans]
    basenet = str(OCT1) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) + basemask
    
    if subnetansnum == 1:
        OCT2 = OCT2
        maskans = '/13'
    elif subnetansnum == 2:
        OCT2 += 8
        maskans = '/14'
    elif subnetansnum == 3:
        OCT2 += 12
        maskans = '/15'
    elif subnetansnum == 4:
        OCT2 += 14
        maskans = '/16'
    elif subnetansnum == 5:
        OCT2 += 15
        maskans = '/17'
    elif subnetansnum == 6:
        OCT2 += 15
        OCT3 += 128 
        maskans = '/17'
        
    ansnet = str(OCT1) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) + maskans
   
    file.write("FIB" + '\t'  + "Given the base network of " + str(basenet) + " and the hosts requirements of " + str(subnethostnum) + " use vlsm and best practices to create the necessary subnets. What is the network and cdir (1.2.3.4/24) of the " + ordinal(subnetansnum) + " subnet you created." + '\t' + str(ansnet) + "\n")

    BASEOCT2 += 16 
    number += 1
     
file.close()
"""


"""
# vlsm questions basenet = 192.168.0.0/25 with host requirements of
# 50, 25, 10, 10. Asks students for one of the
# subnets randomly (1 - 4). Should always expect the same single answer
# because all IPs in the basenet are used.
file = open('vlsm_25.txt','a') 

BASEOCT1 = 192
BASEOCT2 = 168
BASEOCT3 = 0
BASEOCT4 = 0

OCT1 = BASEOCT1
OCT2 = BASEOCT2
OCT3 = BASEOCT3
OCT4 = BASEOCT4

basemask = '/25'
subnethostnum = ['50', '25', '10', '10']
while BASEOCT3 <= 255:
    while BASEOCT4 <= 128:
        OCT1 = BASEOCT1
        OCT2 = BASEOCT2
        OCT3 = BASEOCT3
        OCT4 = BASEOCT4
        subnetans = random.randint(0, 3) # to pull from list
        subnetansnum = subnetans + 1 # translate to a nth spot.
        hostans = subnethostnum[subnetans]
        basenet = str(OCT1) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) + basemask
    
        if subnetansnum == 1:
            OCT4 = OCT4
            maskans = '/26'
        elif subnetansnum == 2:
            OCT4 += 64
            maskans = '/27'
        elif subnetansnum == 3:
            OCT4 += 96
            maskans = '/28'
        elif subnetansnum == 4:
            OCT4 += 112
            maskans = '/28'

        
        ansnet = str(OCT1) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) + maskans
   
        file.write("FIB" + '\t'  + "Given the base network of " + str(basenet) + " and the hosts requirements of " + str(subnethostnum) + " use vlsm and best practices to create the necessary subnets. What is the network and cdir (1.2.3.4/24) of the " + ordinal(subnetansnum) + " subnet you created." + '\t' + str(ansnet) + "\n")
        
        #print(basenet, hostans, subnetansnum, ansnet, number)
        BASEOCT4 += 128
        number += 1
        
    BASEOCT4 = 0
    BASEOCT3 += 1
     
file.close()
"""

"""
# vlsm questions basenet = 172.16.0.0/21 with host requirements of
# 1000, 500, 200, 100, 50, 35, 10, 10. Asks students for one of the
# subnets randomly (1 - 8). Should always expect the same single answer
# because all IPs in the basenet are used.
file = open('vlsm_21.txt','a') 

BASEOCT1 = 172
BASEOCT2 = 16
BASEOCT3 = 0
BASEOCT4 = 0

OCT1 = BASEOCT1
OCT2 = BASEOCT2
OCT3 = BASEOCT3
OCT4 = BASEOCT4

basemask = '/21'
subnethostnum = ['1000', '500', '200', '100', '50', '35', '10', '10']
while BASEOCT2 <= 31:
    while BASEOCT3 <= 248:
        OCT1 = BASEOCT1
        OCT2 = BASEOCT2
        OCT3 = BASEOCT3
        OCT4 = BASEOCT4
        subnetans = random.randint(0, 7) # to pull from list
        subnetansnum = subnetans + 1 # translate to a nth spot.
        hostans = subnethostnum[subnetans]
        basenet = str(OCT1) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) + basemask
    
        if subnetansnum == 1:
            OCT3 = OCT3
            OCT4 = OCT4
            maskans = '/22'
        elif subnetansnum == 2:
            OCT3 += 4
            OCT4 = OCT4
            maskans = '/23'
        elif subnetansnum == 3:
            OCT3 += 6
            OCT4 = OCT4
            maskans = '/24'
        elif subnetansnum == 4:
            OCT3 += 7
            OCT4 = OCT4
            maskans = '/25'
        if subnetansnum == 5:
            OCT3 += 7
            OCT4 = 128
            maskans = '/26'
        elif subnetansnum == 6:
            OCT3 += 7
            OCT4 = 192
            maskans = '/27'
        elif subnetansnum == 7:
            OCT3 += 7
            OCT4 = 224
            maskans = '/28'
        elif subnetansnum == 8:
            OCT3 += 7
            OCT4 = 240
            maskans = '/28'

        
        ansnet = str(OCT1) + "." + str(OCT2) + "." + str(OCT3) + "." + str(OCT4) + maskans
   
        file.write("FIB" + '\t'  + "Given the base network of " + str(basenet) + " and the hosts requirements of " + str(subnethostnum) + " use vlsm and best practices to create the necessary subnets. What is the network and cdir (1.2.3.4/24) of the " + ordinal(subnetansnum) + " subnet you created." + '\t' + str(ansnet) + "\n")
        
        #print(basenet, hostans, subnetansnum, ansnet, number)
        BASEOCT3 += 8
        number += 1
        
    BASEOCT3 = 0
    BASEOCT2 += 1
     
file.close()
"""

"""
# network subnet summerzation questions 
file = open('netsummer.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randlargernet()
    IPaddr = information[4]
    Mask = information[0]
    Supernet = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
    
    newmasknum = Masknum + random.randint(1, 3)
    subnets = Supernet.subnets(new_prefix=newmasknum)
    subnetlist =[]
    
    for x in subnets:
        subnetlist.append(x.with_prefixlen)
    
    print(subnetlist)
    file.write("FIB" + '\t'  + "Enter the network that contains all of the following subnets: " + str(subnetlist) + "." + '\t' + str(Supernet) + "\n")
    print(number)
    number += 1  
file.close()
"""

# host subnet summerzation questions 
file = open('hostsummer.txt','a') 
#random = random.randint(1, 255)w
number = 0
while  number <= 999:
    information = randlargernet()
    IPaddr = information[4]
    Mask = information[0]
    Supernet = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
    
    newmasknum = Masknum + random.randint(1, 3)
    subnets = Supernet.subnets(new_prefix=newmasknum)
    hostsubnetlist =[]
    
    for x in subnets:
        maxhosts = ipaddress.ip_network(x, strict=False).num_addresses - 1
        hostip = x[random.randint(0, maxhosts)]
        hostsubnetlist.append(str(hostip) + "/" + str(newmasknum))
    
    print(hostsubnetlist)
    file.write("FIB" + '\t'  + "Enter the network that contains all of the following subneted hosts: " + str(hostsubnetlist) + "." + '\t' + str(Supernet) + "\n")
    print(number)
    number += 1  
file.close()

"""
# ABC network subnet summerzation questions 
file = open('abcnetsummer.txt','a') 
#random = random.randint(1, 255)
number = 0
while  number <= 999:
    information = randABClargernet()
    IPaddr = information[4]
    Mask = information[0]
    Supernet = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
    
    newmasknum = Masknum + random.randint(1, 3)
    subnets = Supernet.subnets(new_prefix=newmasknum)
    subnetlist =[]
    
    for x in subnets:
        subnetlist.append(x.with_prefixlen)
    
    print(subnetlist)
    file.write("FIB" + '\t'  + "Enter the network that contains all of the following subnets: " + str(subnetlist) + "." + '\t' + str(Supernet) + "\n")
    print(number)
    number += 1  
file.close()
"""

"""
# ABC host subnet summerzation questions 
file = open('abchostsummer.txt','a') 
#random = random.randint(1, 255)w
number = 0
while  number <= 999:
    information = randABClargernet()
    IPaddr = information[4]
    Mask = information[0]
    Supernet = information[1]
    Broadcast = information[2]
    Masknum = information[5]
    subnetmask = information[3]
    
    newmasknum = Masknum + random.randint(1, 3)
    subnets = Supernet.subnets(new_prefix=newmasknum)
    hostsubnetlist =[]
    
    for x in subnets:
        maxhosts = ipaddress.ip_network(x, strict=False).num_addresses - 1
        hostip = x[random.randint(0, maxhosts)]
        hostsubnetlist.append(str(hostip) + "/" + str(newmasknum))
    
    print(hostsubnetlist)
    file.write("FIB" + '\t'  + "Enter the network that contains all of the following subneted hosts: " + str(hostsubnetlist) + "." + '\t' + str(Supernet) + "\n")
    print(number)
    number += 1  
file.close()
"""


























