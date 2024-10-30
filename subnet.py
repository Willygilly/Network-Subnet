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
    


netAddr,firstUseAddr,lastAddr,broadAddr = subnet('2.134.76.78',26)
#problem 1
p1Network = netAddr
p1Broadcast = broadAddr
p1First = firstUseAddr
p1Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('169.119.38.121',24)
#problem 2
p2Network = netAddr
p2Broadcast = broadAddr
p2First = firstUseAddr
p2Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('80.105.255.163',27)
#problem 3
p3Network = netAddr
p3Broadcast = broadAddr
p3First = firstUseAddr
p3Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('247.90.217.205',25)
#problem 4
p4Network = netAddr
p4Broadcast = broadAddr
p4First = firstUseAddr
p4Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('157.75.179.248',28)
#problem 5
p5Network = netAddr
p5Broadcast = broadAddr
p5First = firstUseAddr
p5Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('69.60.141.34',26)
#problem 6
p6Network = netAddr
p6Broadcast = broadAddr
p6First = firstUseAddr
p6Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('236.45.102.77',29)
#problem 7
p7Network = netAddr
p7Broadcast = broadAddr
p7First = firstUseAddr
p7Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('147.30.64.119',27)
#problem 8
p8Network = netAddr
p8Broadcast = broadAddr
p8First = firstUseAddr
p8Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('58.15.26.162',24)
#problem 9
p9Network = netAddr
p9Broadcast = broadAddr
p9First = firstUseAddr
p9Last = lastAddr

netAddr,firstUseAddr,lastAddr,broadAddr = subnet('225.0.244.204',27)
#problem 10
p10Network = netAddr
p10Broadcast = broadAddr
p10First = firstUseAddr
p10Last = lastAddr
