#enter your unique code
uniquecode = 76334 
def subnet(ipaddr,cidr):
    subNetHosts = (2**(32 - cidr)) # There are 256 available hosts
    octet = list(map(int,ipaddr.split('.'))) # split, apply binary then join again
    octetBit = ''.join(list(map(lambda x: format(x,'b').rjust(8,'0'),octet))) # formating and padding  converting ip address to binary

    hostBitMask = format(subNetHosts,'b').rjust(32,'1')
    netBitMasking = format(int(hostBitMask,2) & int(octetBit,2),'b').rjust(32,'0')
    netAddrBit = f"{netBitMasking[0:8]}.{netBitMasking[8:16]}.{netBitMasking[16:24]}.{netBitMasking[24:32]}"
    netAddr = '.'.join(list(map(lambda x: str(int(x,2)),netAddrBit.split('.'))))

    broadBitMasking= netBitMasking[0:cidr].ljust(32,'1')
    broadAddrBit = f"{broadBitMasking[0:8]}.{broadBitMasking[8:16]}.{broadBitMasking[16:24]}.{broadBitMasking[24:32]}"
    broadAddr = '.'.join(list(map(lambda x: str(int(x,2)),broadAddrBit.split('.'))))

    firstUseAddr = f"{netAddr[0:netAddr.rindex('.')]}.{eval(f"{netAddr[netAddr.rindex('.')+1::]}+1")}" # slice the prefix, add/evalaute the octet of interetst
    lastUseAddr =  f"{broadAddr[0:broadAddr.rindex('.')]}.{eval(f"{broadAddr[broadAddr.rindex('.')+1::]}-1")}"

    return netAddr, firstUseAddr, lastUseAddr, broadAddr
    


netAddr,firstAddr,lastAddr,broadAddr = subnet('2.134.76.78',26)
#problem 1
p1Network = f'{netAddr}'
p1Broadcast = f'{broadAddr}'
p1First = f'{firstAddr}'
p1Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('169.119.38.121',24)
#problem 2
p2Network = f'{netAddr}'
p2Broadcast = f'{broadAddr}'
p2First = f'{firstAddr}'
p2Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('80.105.255.163',27)
#problem 3
p3Network = f'{netAddr}'
p3Broadcast = f'{broadAddr}'
p3First = f'{firstUseAddr}'
p3Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('247.90.217.205',25)
#problem 4
p4Network = f'{netAddr}'
p4Broadcast = f'{broadAddr}'
p4First = f'{firstUseAddr}'
p4Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('157.75.179.248',28)
#problem 5
p5Network = f'{netAddr}'
p5Broadcast = f'{broadAddr}'
p5First = f'{firstUseAddr}'
p5Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('69.60.141.34',26)
#problem 6
p6Network = f'{netAddr}'
p6Broadcast = f'{broadAddr}'
p6First = f'{firstUseAddr}'
p6Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('236.45.102.77',29)
#problem 7
p7Network = f'{netAddr}'
p7Broadcast = f'{broadAddr}'
p7First = f'{firstUseAddr}'
p7Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('147.30.64.119',27)
#problem 8
p8Network = f'{netAddr}'
p8Broadcast = f'{broadAddr}'
p8First = f'{firstUseAddr}'
p8Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('58.15.26.162',24)
#problem 9
p9Network = f'{netAddr}'
p9Broadcast = f'{broadAddr}'
p9First = f'{firstUseAddr}'
p9Last = f'{lastAddr}'

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('225.0.244.204',27)
#problem 10
p10Network = f'{netAddr}'
p10Broadcast = f'{broadAddr}'
p10First = f'{firstUseAddr}'
p10Last = f'{lastAddr}'



"""
example:

uniquecode = 12345

problem 1
p1Network = '199.204.14.128'
p1Broadcast = '199.204.14.255'
p1First = '199.204.14.129'
p1Last =  '199.204.14.254'
"""
